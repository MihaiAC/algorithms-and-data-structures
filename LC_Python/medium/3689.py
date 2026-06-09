from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        cMax, cMin = -1, 5 * 10**9 + 1
        for num in nums:
            if num < cMin:
                cMin = num

            if num > cMax:
                cMax = num

        return (cMax - cMin) * k
