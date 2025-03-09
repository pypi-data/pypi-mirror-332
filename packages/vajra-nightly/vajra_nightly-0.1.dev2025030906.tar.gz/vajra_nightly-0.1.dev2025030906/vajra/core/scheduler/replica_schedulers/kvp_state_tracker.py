from collections import OrderedDict, defaultdict
from math import ceil
from typing import Dict, List, Optional, Tuple

from vajra._native.core import BlockSpaceManager  # type: ignore
from vajra.config import CacheConfig, ModelConfig, ParallelConfig
from vajra.datatypes import Sequence
from vajra.logger import init_logger

logger = init_logger(__name__)

ALLOCATION_MAX_TOKEN_THRESHOLD = 500


class _KVPBatchTracker:
    """
    Tracks KVP-specific batch information for a scheduling cycle.
    This class is internal to KVPStateTracker and not meant to be used directly.
    """

    def __init__(self, kvp_size: int):
        self.kvp_size = kvp_size

        # Per KVP group tracking
        self.per_kvp_group_sequences: List[List[Sequence]] = [
            [] for _ in range(kvp_size)
        ]
        self.per_kvp_group_num_q_tokens: List[List[int]] = [[] for _ in range(kvp_size)]
        self.per_kvp_group_num_kv_tokens: List[List[int]] = [
            [] for _ in range(kvp_size)
        ]
        self.per_kvp_group_num_active_kvp_groups: List[List[int]] = [
            [] for _ in range(kvp_size)
        ]
        self.per_kvp_group_last_kvp_group_ids: List[List[int]] = [
            [] for _ in range(kvp_size)
        ]
        self.per_kvp_group_seq_num_processed_tokens: List[List[int]] = [
            [] for _ in range(kvp_size)
        ]
        self.per_kvp_group_total_num_q_tokens: List[int] = [0 for _ in range(kvp_size)]

    def add_sequence(
        self,
        seq: Sequence,
        num_q_tokens: int,
        active_kvp_group_ids: List[int],
        kv_token_info: List[Tuple[int, int, bool]],
        num_processed_tokens: int,
    ) -> None:
        """Add sequence information to the KVP batch tracker"""
        # Update per-group tracking
        for kvp_group_id, num_kv_tokens, _ in kv_token_info:
            self.per_kvp_group_sequences[kvp_group_id].append(seq)
            self.per_kvp_group_num_q_tokens[kvp_group_id].append(num_q_tokens)
            self.per_kvp_group_num_kv_tokens[kvp_group_id].append(num_kv_tokens)
            self.per_kvp_group_num_active_kvp_groups[kvp_group_id].append(
                len(active_kvp_group_ids)
            )
            self.per_kvp_group_seq_num_processed_tokens[kvp_group_id].append(
                num_processed_tokens
            )
            self.per_kvp_group_last_kvp_group_ids[kvp_group_id].append(
                active_kvp_group_ids[-1]
            )
            self.per_kvp_group_total_num_q_tokens[kvp_group_id] += num_q_tokens

    def _get_q_tokens_for_kvp_groups(
        self, active_kvp_group_ids: List[int]
    ) -> List[int]:
        """Get the number of Q tokens for the given KVP groups"""
        return [
            self.per_kvp_group_total_num_q_tokens[kvp_group_id]
            for kvp_group_id in active_kvp_group_ids
        ]

    def get_free_kvp_groups(
        self, token_threshold: int = ALLOCATION_MAX_TOKEN_THRESHOLD
    ) -> List[int]:
        """Get KVP groups that are not busy (have few Q tokens)"""
        return [
            kvp_group_id
            for kvp_group_id in range(self.kvp_size)
            if self.per_kvp_group_total_num_q_tokens[kvp_group_id] < token_threshold
        ]

    def get_per_group_sequences(self, kvp_group_id: int) -> List[Sequence]:
        """Get sequences for a specific KVP group"""
        return self.per_kvp_group_sequences[kvp_group_id]

    def get_per_group_q_tokens(self, kvp_group_id: int) -> List[int]:
        """Get Q tokens for a specific KVP group"""
        return self.per_kvp_group_num_q_tokens[kvp_group_id]

    def get_per_group_kv_tokens(self, kvp_group_id: int) -> List[int]:
        """Get KV tokens for a specific KVP group"""
        return self.per_kvp_group_num_kv_tokens[kvp_group_id]

    def get_per_group_active_kvp_groups(self, kvp_group_id: int) -> List[int]:
        """Get active KVP groups count for sequences in a specific KVP group"""
        return self.per_kvp_group_num_active_kvp_groups[kvp_group_id]

    def get_per_group_last_kvp_group_ids(self, kvp_group_id: int) -> List[int]:
        """Get last KVP group IDs for sequences in a specific KVP group"""
        return self.per_kvp_group_last_kvp_group_ids[kvp_group_id]


class KVPStateTracker:
    def __init__(
        self,
        model_config: ModelConfig,
        cache_config: CacheConfig,
        parallel_config: ParallelConfig,
    ) -> None:
        self.model_config = model_config
        self.cache_config = cache_config
        self.parallel_config = parallel_config

        self.kvp_size = parallel_config.kv_parallel_size

        if self.kvp_size == 1:
            self.max_num_tokens_per_kvp_group = model_config.max_model_len
        else:
            assert parallel_config.max_num_tokens_per_kvp_group is not None
            assert (
                parallel_config.max_num_tokens_per_kvp_group > cache_config.block_size
            )
            assert (
                parallel_config.max_num_tokens_per_kvp_group % cache_config.block_size
                == 0
            )
            self.max_num_tokens_per_kvp_group = (
                parallel_config.max_num_tokens_per_kvp_group
            )

        self.max_num_blocks_per_kvp_group = ceil(
            self.max_num_tokens_per_kvp_group / cache_config.block_size
        )
        self.max_num_blocks_per_kvp_group = min(
            self.max_num_blocks_per_kvp_group, cache_config.num_gpu_blocks
        )

        self.max_seq_len = (
            self.kvp_size * self.max_num_blocks_per_kvp_group * cache_config.block_size
        )

        self.block_managers_map: Dict[int, BlockSpaceManager] = {}
        for i in range(self.kvp_size):
            self.block_managers_map[i] = BlockSpaceManager(
                cache_config.block_size,
                cache_config.num_gpu_blocks,
                model_config.max_model_len,
            )

        self.seq_kvp_group_block_counter: Dict[str, OrderedDict[int, int]] = (
            defaultdict(OrderedDict)
        )
        self.kvp_group_pending_prefill_work: List[int] = [
            0 for _ in range(self.kvp_size)
        ]

        # Create a new batch tracker for each scheduling cycle
        self._current_batch_tracker = None

    def start_batch_formation(self) -> None:
        """Start a new batch formation cycle"""
        self._current_batch_tracker = _KVPBatchTracker(self.kvp_size)

    def get_batch_tracker_q_tokens(self, seq: Sequence) -> List[int]:
        """Get Q tokens for the given KVP groups from the current batch tracker"""
        self._ensure_batch_tracker()
        active_kvp_group_ids = self.get_active_kvp_group_ids(seq)
        return self._current_batch_tracker._get_q_tokens_for_kvp_groups(
            active_kvp_group_ids
        )

    def get_batch_tracker_free_groups(self) -> List[int]:
        """Get KVP groups that are not busy from the current batch tracker"""
        self._ensure_batch_tracker()
        return self._current_batch_tracker.get_free_kvp_groups()

    def add_sequence_to_batch(
        self, seq: Sequence, num_q_tokens: int, active_kvp_group_ids: List[int]
    ) -> None:
        """Add a sequence to the current batch tracker"""
        self._ensure_batch_tracker()
        num_processed_tokens, kv_token_info = self.get_sequence_kv_token_info(
            seq, active_kvp_group_ids
        )
        self._current_batch_tracker.add_sequence(
            seq, num_q_tokens, active_kvp_group_ids, kv_token_info, num_processed_tokens
        )

    def get_batch_tracker_per_group_info(
        self, kvp_group_id: int
    ) -> Tuple[List[Sequence], List[int], List[int], List[int], List[int]]:
        """Get all information for a specific KVP group from the current batch tracker"""
        self._ensure_batch_tracker()
        return (
            self._current_batch_tracker.get_per_group_sequences(kvp_group_id),
            self._current_batch_tracker.get_per_group_q_tokens(kvp_group_id),
            self._current_batch_tracker.get_per_group_kv_tokens(kvp_group_id),
            self._current_batch_tracker.get_per_group_active_kvp_groups(kvp_group_id),
            self._current_batch_tracker.get_per_group_last_kvp_group_ids(kvp_group_id),
        )

    def _ensure_batch_tracker(self) -> None:
        """Ensure that a batch tracker exists"""
        if self._current_batch_tracker is None:
            self.start_batch_formation()

    def get_max_seq_len(self) -> int:
        return self.max_seq_len

    def get_allocation_order(self, kvp_group_ids: List[int]) -> List[int]:
        """
        We are simply picking the kvp group with the least prefill work.
        We use the square of number of prefill tokens as a simple proxy for prefill work of now.
        """
        return sorted(
            kvp_group_ids,
            key=lambda kvp_group_id: self.kvp_group_pending_prefill_work[kvp_group_id],
        )

    def allocate(self, seq: Sequence) -> bool:
        """
        Allocate memory for a sequence across KVP groups.

        Args:
            seq: The sequence to allocate memory for

        Returns:
            bool: True if allocation was successful, False otherwise
        """

        filter_kvp_group_ids = self.get_batch_tracker_free_groups()

        num_blocks = len(seq.logical_token_blocks)
        # if seq is too large, return false
        if num_blocks > self.kvp_size * self.max_num_blocks_per_kvp_group:
            logger.warning(
                f"Ignoring seq_id: {seq.seq_id} due to max num blocks per kvp group limit."
            )
            return False, num_blocks

        # filter the busy kvp groups based on the input filter or create a list of all groups
        available_kvp_group_ids = (
            filter_kvp_group_ids
            if filter_kvp_group_ids is not None
            else list(range(self.kvp_size))
        )

        if not available_kvp_group_ids:
            return False, num_blocks

        # if seq fits in one kvp group, allocate it to first available kvp group
        if num_blocks < self.max_num_blocks_per_kvp_group:
            for kvp_group_id in self.get_allocation_order(available_kvp_group_ids):
                if self.block_managers_map[kvp_group_id].can_allocate_blocks(
                    num_blocks
                ):
                    self.block_managers_map[kvp_group_id].allocate(seq, num_blocks)
                    self.seq_kvp_group_block_counter[seq.seq_id][
                        kvp_group_id
                    ] = num_blocks
                    return True, num_blocks
            return False, num_blocks

        num_kv_parallel_groups = ceil(num_blocks / self.max_num_blocks_per_kvp_group)
        last_group_num_blocks = num_blocks - self.max_num_blocks_per_kvp_group * (
            num_kv_parallel_groups - 1
        )

        num_groups_found = 0
        last_group_found = False
        kvp_group_ids: List[int] = []
        last_kvp_group_id: Optional[int] = None

        for kvp_group_id in self.get_allocation_order(available_kvp_group_ids):
            block_manager = self.block_managers_map[kvp_group_id]
            if block_manager.can_allocate_blocks(self.max_num_blocks_per_kvp_group):
                num_groups_found += 1
                kvp_group_ids.append(kvp_group_id)
            elif (
                last_group_num_blocks
                and not last_group_found
                and block_manager.can_allocate_blocks(last_group_num_blocks)
            ):
                last_group_found = True
                num_groups_found += 1
                last_kvp_group_id = kvp_group_id
            if num_groups_found == num_kv_parallel_groups:
                break

        if num_groups_found != num_kv_parallel_groups:
            return False

        if last_kvp_group_id:
            kvp_group_ids.append(last_kvp_group_id)
        else:
            last_kvp_group_id = kvp_group_ids[-1]

        for kvp_group_id in kvp_group_ids:
            if kvp_group_id == last_kvp_group_id:
                self.block_managers_map[kvp_group_id].allocate(
                    seq, last_group_num_blocks
                )
                self.seq_kvp_group_block_counter[seq.seq_id][
                    kvp_group_id
                ] = last_group_num_blocks
            else:
                self.block_managers_map[kvp_group_id].allocate(
                    seq, self.max_num_blocks_per_kvp_group
                )
                self.seq_kvp_group_block_counter[seq.seq_id][
                    kvp_group_id
                ] = self.max_num_blocks_per_kvp_group

            self.kvp_group_pending_prefill_work[kvp_group_id] += seq.prompt_len**2

        return True, num_blocks

    def free_seq(self, seq: Sequence) -> None:
        """Free all memory allocated for a sequence"""
        if seq.seq_id not in self.seq_kvp_group_block_counter:
            return

        for kvp_group_id in self.seq_kvp_group_block_counter[seq.seq_id]:
            self.block_managers_map[kvp_group_id].free(seq)
        del self.seq_kvp_group_block_counter[seq.seq_id]

    def get_last_kv_group_id(self, seq: Sequence) -> int:
        """Get the last KVP group ID for a sequence"""
        return next(reversed(self.seq_kvp_group_block_counter[seq.seq_id]))

    def can_append_slot(self, seq: Sequence) -> bool:
        """Check if a slot can be appended to the sequence"""
        last_kvp_group_id = self.get_last_kv_group_id(seq)
        return self.block_managers_map[last_kvp_group_id].can_append_slot()

    def append_slot(self, seq: Sequence, num_total_blocks: int) -> bool:
        """Increment the block counter if a new block has been allocated"""
        last_kvp_group_id = self.get_last_kv_group_id(seq)
        has_appended = self.block_managers_map[last_kvp_group_id].append_slot(
            seq, num_total_blocks
        )
        self.seq_kvp_group_block_counter[seq.seq_id][last_kvp_group_id] += int(
            has_appended
        )
        return has_appended

    def get_active_kvp_group_ids(self, seq: Sequence) -> List[int]:
        """Get the active KVP group IDs for a sequence"""
        kvp_group_ids = list(self.seq_kvp_group_block_counter[seq.seq_id])

        if seq.prompt_processing_finished:
            return kvp_group_ids

        num_processed_tokens = seq.get_num_tokens_stage_processed()
        num_groups = num_processed_tokens // self.max_num_tokens_per_kvp_group + 1
        return kvp_group_ids[:num_groups]

    def update_prefill_work(self, seq, current_tokens: int, new_tokens: int) -> None:
        """Update the pending prefill work for KVP groups based on token count changes"""
        kvp_group_ids = self.get_active_kvp_group_ids(seq)
        work_delta = (current_tokens + new_tokens) ** 2 - current_tokens**2
        for kvp_group_id in kvp_group_ids:
            self.kvp_group_pending_prefill_work[kvp_group_id] -= work_delta

    def get_kvp_group_block_counter(self, seq_id: str) -> OrderedDict[int, int]:
        """Get the block counter for a sequence across KVP groups"""
        return self.seq_kvp_group_block_counter[seq_id]

    def get_sequence_kv_token_info(
        self, seq: Sequence, active_kvp_group_ids: List[int]
    ) -> Tuple[int, List[Tuple[int, int, bool]]]:
        """
        Get KV token information for a sequence.

        Returns:
            Tuple containing:
            - Number of processed tokens
            - List of tuples (kvp_group_id, num_kv_tokens, is_last_group)
        """
        num_processed_tokens = seq.get_num_tokens_stage_processed()
        kv_token_info = []

        for i, kvp_group_id in enumerate(active_kvp_group_ids):
            is_last_group = i == len(active_kvp_group_ids) - 1

            if is_last_group:
                num_kv_tokens_in_other_groups = (
                    len(active_kvp_group_ids) - 1
                ) * self.max_num_tokens_per_kvp_group
                num_kv_tokens = num_processed_tokens - num_kv_tokens_in_other_groups
            else:
                num_kv_tokens = self.max_num_tokens_per_kvp_group

            assert num_kv_tokens >= 0
            kv_token_info.append((kvp_group_id, num_kv_tokens, is_last_group))

        return num_processed_tokens, kv_token_info
