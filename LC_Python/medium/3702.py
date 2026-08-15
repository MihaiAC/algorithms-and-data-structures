from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        all_zeros = True
        curr_xor = 0

        for num in nums:
            if num > 0:
                all_zeros = False

            curr_xor ^= num

        return len(nums) if curr_xor != 0 else len(nums) - 1 if not all_zeros else 0


sol = Solution()
print(sol.longestSubsequence([1, 2, 3]))
print(sol.longestSubsequence([2, 3, 4]))
