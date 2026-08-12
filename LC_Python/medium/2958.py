from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        N = len(nums)
        curr_window = defaultdict(int)
        max_len = 0

        for right in range(N):
            curr_window[nums[right]] += 1

            while curr_window[nums[right]] > k:
                curr_window[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


sol = Solution()
print(sol.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
print(sol.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1))
print(sol.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4))
