from random import randint
from collections import deque


class RandomizedSet:
    def __init__(self):
        self.key_to_idx = dict()
        self.idx_to_key = deque()

    def insert(self, val: int) -> bool:
        if val in self.key_to_idx:
            return False
        else:
            nr_vals = len(self.key_to_idx)
            self.key_to_idx[val] = nr_vals
            self.idx_to_key.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.key_to_idx:
            return False
        else:
            if len(self.key_to_idx) == 1:
                self.key_to_idx = dict()
                self.idx_to_key = deque()
            else:
                val_idx = self.key_to_idx[val]
                len_idx = len(self.key_to_idx) - 1

                if val_idx == len_idx:
                    self.idx_to_key.pop()
                    del self.key_to_idx[val]
                else:
                    len_key = self.idx_to_key[len_idx]

                    self.idx_to_key.pop()
                    del self.key_to_idx[val]

                    self.key_to_idx[len_key] = val_idx
                    self.idx_to_key[val_idx] = len_key

            return True

    def getRandom(self) -> int:
        idx = randint(0, len(self.key_to_idx) - 1)
        return self.idx_to_key[idx]
