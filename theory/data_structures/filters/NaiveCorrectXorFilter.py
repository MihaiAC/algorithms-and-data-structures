import mmh3
import numpy as np
from math import ceil
from collections import deque
from typing import List, Tuple


class XorFilter:
    """
    Naive xor filter. 60% acc
    """

    def __init__(self, expected_nr_items: int):
        # Number of slots (bits)
        self.n_bits = ceil(1.23 * expected_nr_items + 32)

        # Fingerprint array
        self.filter = [0] * self.n_bits

        # Counters
        self.curr_n_elems = 0
        self.current_fp = 0
        self.current_tn = 0
        self.current_fn = 0
        self.current_tp = 0

        # Fallback set used strictly for stats (not logic)
        self.elems = set()

        # Hash seeds - Randomized to allow for retries
        self.index_seeds = [
            np.random.randint(0, 100000),
            np.random.randint(0, 100000),
            np.random.randint(0, 100000),
        ]
        self.fingerprint_seed = np.random.randint(0, 100000)

    def _get_fingerprint(self, item: int) -> int:
        """Helper to calculate an item's fingerprint."""
        # Using a 16-bit fingerprint for a lower theoretical false positive rate
        return mmh3.hash(str(item), self.fingerprint_seed) & 0xFFFF

    def item_to_slots(self, item: int) -> List[int]:
        """Compute three positions from hashes. Naive way of doing hashing for a xor filter."""
        slots = []
        for seed in self.index_seeds:
            index = mmh3.hash(str(item), seed) % self.n_bits
            slots.append(index)
        return slots

    def build_filter(self, items: List[int]):
        """
        Build the filter properly, via a naive version of the proper hypergraph
        peeling + reverse assignment of fingerprints.
        """
        N_items = len(items)

        # Build hypergraph.
        item_id_to_value = list(items)
        item_id_to_slots = [self.item_to_slots(item) for item in items]
        slot_to_item_ids = [[] for _ in range(self.n_bits)]
        slot_degree = [0] * self.n_bits

        for item_id, slots in enumerate(item_id_to_slots):
            for slot in slots:
                slot_to_item_ids[slot].append(item_id)
                slot_degree[slot] += 1

        # Peeling process - find slots with degree 1, record (item_id, free_slot).
        peel_queue = deque(i for i, deg in enumerate(slot_degree) if deg == 1)
        peel_order: List[Tuple[int, int]] = []  # stores (item_id, free_slot)
        removed = [False] * N_items

        while peel_queue:
            popped_slot = peel_queue.popleft()
            if slot_degree[popped_slot] != 1:
                continue

            # Find the single unremoved item touching this slot
            item_id = -1
            for item_id_candidate in slot_to_item_ids[popped_slot]:
                if not removed[item_id_candidate]:
                    item_id = item_id_candidate
                    break

            if item_id == -1:
                continue

            peel_order.append((item_id, popped_slot))
            removed[item_id] = True

            # Remove the item and update degrees of touching slots
            for slot in item_id_to_slots[item_id]:
                if slot != popped_slot:
                    slot_degree[slot] -= 1
                    if slot_degree[slot] == 1:
                        peel_queue.append(slot)

        # If we didn't peel all the items => failure, need to start again with other seeds.
        if len(peel_order) != N_items:
            raise RuntimeError("Peeling failed: try new hash seeds, or larger table.")

        # Reverse assignment - set filter values for each slot.
        for item_id, free_slot in reversed(peel_order):
            item, slots = item_id_to_value[item_id], item_id_to_slots[item_id]
            fingerprint = self._get_fingerprint(item)

            xor_sum = 0
            for slot in slots:
                if slot != free_slot:
                    xor_sum ^= self.filter[slot]

            # Assign free_slot so XOR of triple = fingerprint
            self.filter[free_slot] = xor_sum ^ fingerprint

        self.elems = set(items)
        self.curr_n_elems = len(items)

    def contains(self, item: int) -> bool:
        """Query the filter + track stats using self.elems."""
        slots = self.item_to_slots(item)

        # Reconstruct fingerprint.
        constructed_fingerprint = 0
        for slot in slots:
            constructed_fingerprint ^= self.filter[slot]

        # TODO: extract this into a calc fingerprint function
        actual_fingerprint = self._get_fingerprint(item)

        is_present = constructed_fingerprint == actual_fingerprint

        if is_present:
            if item in self.elems:
                self.current_tp += 1
            else:
                self.current_fp += 1
        else:
            if item in self.elems:
                self.current_fn += 1  # This should now be 0
            else:
                self.current_tn += 1
        return is_present

    def calculate_fpr(self) -> float:
        """Observed false-positive rate."""
        total = self.current_fp + self.current_tn
        return (self.current_fp / total) if total else 0.0

    def calculate_fnr(self) -> float:
        """Observed false-negative rate."""
        total = self.current_fn + self.current_tp
        return (self.current_fn / total) if total else 0.0

    def calculate_accuracy(self) -> float:
        """Observed overall accuracy: (TP + TN) / total queries."""
        total = self.current_tp + self.current_tn + self.current_fp + self.current_fn
        return ((self.current_tp + self.current_tn) / total) if total else 0.0


if __name__ == "__main__":
    MAXN = 10000
    N = 4000

    numbers_to_add = list(np.random.choice(MAXN, size=N, replace=False))

    # Build a for loop up to N_RETRIES that tries out different seeds
    MAX_RETRIES = 100
    xor_filter = None
    build_successful = False

    print(f"Attempting to build filter for {N} items...")
    for i in range(MAX_RETRIES):
        try:
            temp_filter = XorFilter(N)  # new instance => fresh seeds
            temp_filter.build_filter(numbers_to_add)

            xor_filter = temp_filter
            build_successful = True
            print(f"Successfully built filter on attempt {i + 1}.")
            break
        except RuntimeError as e:
            print(f"Attempt {i + 1} failed: {e}")

    if not build_successful:
        raise RuntimeError(f"Could not build the filter after {MAX_RETRIES} attempts.")

    # Test the filter
    for item in range(MAXN):
        xor_filter.contains(item)

    # Print out all metrics
    print("\n--- Filter Performance ---")
    print(f"Inserted items: {xor_filter.curr_n_elems}")
    print(f"True positives: {xor_filter.current_tp}")
    print(f"False positives: {xor_filter.current_fp}")
    print(f"True negatives: {xor_filter.current_tn}")
    print(f"False negatives: {xor_filter.current_fn}")
    print(f"False-positive rate (FPR): {xor_filter.calculate_fpr():.6f}")
    print(f"False-negative rate (FNR): {xor_filter.calculate_fnr():.6f}")
    print(f"Accuracy: {xor_filter.calculate_accuracy():.6f}")
