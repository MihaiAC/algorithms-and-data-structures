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
                len_idx = len(self.key_to_idx)-1

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
        idx = randint(0, len(self.key_to_idx)-1)
        return self.idx_to_key[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom().

if __name__ == '__main__':
    calls = []

    rset = None
    ans_random = []
    our_random = []

    # print(calls[9625])
    # print(values[9625])
    # print(ans[9625])

    for ii, call in enumerate(calls):
        if call == "RandomizedSet":
            rset = RandomizedSet()
        elif call == "insert":
            if rset.insert(values[ii][0]) != ans[ii]:
                print(ii)
                print(ans[ii])
        elif call == "remove":
            if rset.remove(values[ii][0]) != ans[ii]:
                print(ii)
                print(ans[ii])
        else:
            our_random.append(rset.getRandom())
            ans_random.append(ans[ii])