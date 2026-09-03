from typing import List


class Solution:
    def uniformArray(self, nums: List[int]) -> bool:
        smallest = min(nums)
        if smallest % 2 == 0:
            return all([num % 2 == 0 for num in nums])
        return True
