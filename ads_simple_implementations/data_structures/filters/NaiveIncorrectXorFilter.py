import mmh3
from math import ceil
from typing import List
import numpy as np


class XorFilter:
    """
    Naive xor filter. 60% acc
    """

    def __init__(self, expected_nr_items: int):
        # Number of slots (bits) — oversize to reduce collisions
        self.n_bits = ceil(1.5 * expected_nr_items)

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

        # Hash seeds
        self.index_seeds = [1, 2, 3]
        self.fingerprint_seed = 99

    def item_to_index_list(self, item: int) -> List[int]:
        """Compute three positions from hashes."""
        index_list = []
        for seed in self.index_seeds:
            index = mmh3.hash(str(item), seed) % self.n_bits
            index_list.append(index)
        return index_list

    def add_item(self, item: int):
        """XOR an 8-bit fingerprint into three slots."""
        # Fingerprint = keep only the lowest 8 bits of the item hash.
        fingerprint = mmh3.hash(str(item), self.fingerprint_seed) & 0xFF
        for idx in self.item_to_index_list(item):
            self.filter[idx] ^= fingerprint
        self.elems.add(item)
        self.curr_n_elems += 1

    def contains(self, item: int) -> bool:
        """Reconstruct and compare fingerprint; track stats using self.elems."""
        # If any slot is zero, it's definitely not present
        for idx in self.item_to_index_list(item):
            if self.filter[idx] == 0:
                # Cheating.
                if item in self.elems:
                    # False negatives - should not happen in a correct xor filter.
                    self.current_fn += 1
                else:
                    self.current_tn += 1
                return False

        # Reconstruct fingerprint from slots
        # Since I don't construct it correctly, not guaranteed to work.
        combined = 0
        for idx in self.item_to_index_list(item):
            combined ^= self.filter[idx]

        actual_fp = mmh3.hash(str(item), self.fingerprint_seed) & 0xFF
        if combined == actual_fp:
            if item in self.elems:
                self.current_tp += 1
            else:
                self.current_fp += 1
            return True

        if item in self.elems:
            self.current_fn += 1
        else:
            self.current_tn += 1
        return False

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

    xor_filter = XorFilter(N)
    numbers_to_add = list(np.random.choice(MAXN, size=N, replace=False))
    for item in numbers_to_add:
        xor_filter.add_item(item)

    for item in range(MAXN):
        xor_filter.contains(item)

    # Print out all metrics
    print(f"Inserted items: {xor_filter.curr_n_elems}")
    print(f"True positives: {xor_filter.current_tp}")
    print(f"False positives: {xor_filter.current_fp}")
    print(f"True negatives: {xor_filter.current_tn}")
    print(f"False negatives: {xor_filter.current_fn}")
    print(f"False-positive rate (FPR): {xor_filter.calculate_fpr():.6f}")
    print(f"False-negative rate (FNR): {xor_filter.calculate_fnr():.6f}")
    print(f"Accuracy: {xor_filter.calculate_accuracy():.6f}")
