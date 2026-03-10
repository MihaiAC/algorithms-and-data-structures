from typing import List, Tuple
from collections import defaultdict

class Helper:
    def __init__(self, x: int) -> None:
        self.x: int = x
        self.result: int = 0
        self.large: SortedSet = SortedSet()
        self.small: SortedSet = SortedSet()
        self.occ: defaultdict[int, int] = defaultdict(int)
    
    def insert(self, num: int) -> None:
        if self.occ[num] > 0:
            self.internal_remove((self.occ[num], num))
        self.occ[num] += 1
        self.internal_insert((self.occ[num], num))
    
    def remove(self, num: int) -> None:
        self.internal_remove((self.occ[num], num))
        self.occ[num] -= 1
        if self.occ[num] > 0:
            self.internal_insert((self.occ[num], num))
    
    def get(self) -> int:
        return self.result
    
    def internal_insert(self, pair: Tuple[int, int]) -> None:
        if len(self.large) < self.x or pair > self.large[0]:
            self.result += pair[0] * pair[1]
            self.large.add(pair)
            if len(self.large) > self.x:
                to_remove = self.large[0]
                self.result -= to_remove[0] * to_remove[1]
                self.large.remove(to_remove)
                self.small.add(to_remove)
        else:
            self.small.add(pair)
    
    def internal_remove(self, pair: Tuple[int, int]) -> None:
        if pair >= self.large[0]:
            self.result -= pair[0] * pair[1]
            self.large.remove(pair)
            if self.small:
                to_add = self.small[-1]
                self.result += to_add[0] * to_add[1]
                self.small.remove(to_add)
                self.large.add(to_add)
        else:
            self.small.remove(pair)

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        helper: Helper = Helper(x)
        ans: List[int] = []
        for ii in range(len(nums)):
            helper.insert(nums[ii])
            if ii >= k:
                helper.remove(nums[ii-k])
            if ii >= k-1:
                ans.append(helper.get())
        return ans
