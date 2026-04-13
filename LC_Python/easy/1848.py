from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = len(nums)

        for idx, num in enumerate(nums):
            if num == target:
                ans = min(ans, abs(idx - start))

        return ans
