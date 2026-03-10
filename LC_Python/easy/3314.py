from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            res, d = -1, 1
            while num & d:
                res = num - d
                d = d << 1
            ans.append(res)

        return ans
