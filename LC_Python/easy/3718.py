from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        curr = k
        while curr in nums:
            curr += k

        return curr


sol = Solution()
print(sol.missingMultiple([8, 2, 3, 4, 6], 2))
print(sol.missingMultiple([1, 4, 7, 10, 15], 5))
