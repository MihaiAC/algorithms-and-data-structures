from typing import List
from functools import reduce

MODN = 10**9 + 7


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for left, right, k, v in queries:
            for idx in range(left, right + 1, k):
                nums[idx] = (nums[idx] * v) % MODN

        return reduce(lambda a, b: a ^ b, nums, 0)
