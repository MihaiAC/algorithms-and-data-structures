import mmh3
from math import log, ceil
from typing import List

class BloomFilter():
    def __init__(self, expected_nr_items: int, target_fpr: float):
        # Expected maximum number of items the filter will contain.
        self.max_n_elems = expected_nr_items

        # Acceptable false positive rate.
        self.target_fpr = target_fpr

        # Recommended number of bits for n, fpr.
        self.n_bits = ceil(-self.max_n_elems * log(self.target_fpr) / (log(2)**2))

        # Recommended number of hash functions for n, fpr.
        self.n_hashes = ceil(self.n_bits/self.max_n_elems)

        self.curr_n_elems = 0
        self.filter = [0 for _ in range(self.n_bits)]

        # Placeholder for a data structure with much more expensive reads.
        self.elems = set()
        
        self.current_fp = 0
        self.current_tn = 0
    
    def item_to_idx_list(self, item: int) -> List[int]:
        idx_list = []
        for hash_nr in range(1, self.n_hashes+1):
            idx_list.append((hash(item) + hash_nr * mmh3.hash(str(item))) % self.n_bits)
        return idx_list

    def add_item(self, item: int):
        idx_list = self.item_to_idx_list(item)
        for idx in idx_list:
            self.filter[idx] = 1
        self.elems.add(item)
    
    def contains(self, item: int) -> bool:
        for idx in self.item_to_idx_list(item):
            if self.filter[idx] != 1:
                self.current_tn += 1
                return False
        
        # Perform the expensive search operation.
        if item in self.elems:
            return True
        self.current_fp += 1
        return False
    
    def calculate_fpr(self) -> float:
        if self.current_fp > 0 or self.current_tn > 0:
            return self.current_fp / (self.current_fp + self.current_tn)
    
if __name__ == '__main__':
    import numpy as np
    MAXN = 10000
    N = 4000
    P = 0.005
    
    bloom_filter = BloomFilter(N, P)
    numbers_to_add = set(np.random.choice(MAXN, size=N, replace=False))
    for item in numbers_to_add:
        bloom_filter.add_item(item)
    
    for item in range(MAXN):
        is_in_bloom_filter_expected = item in numbers_to_add
        is_in_bloom_filter_actual = bloom_filter.contains(item)
        if is_in_bloom_filter_actual != is_in_bloom_filter_expected:
            print(f"Error for item {item}; expected in bloom filter {is_in_bloom_filter_expected}, actual {is_in_bloom_filter_actual}")
    
    print(f"FPR: {bloom_filter.calculate_fpr()}")