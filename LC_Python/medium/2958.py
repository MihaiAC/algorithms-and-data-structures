from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        N = len(nums)
        curr_window = defaultdict(int)
        max_len = 0

        while True:
            # Expand window.
            while right < N:
                if curr_window[nums[right]] < k:
                    curr_window[nums[right]] += 1
                    right += 1
                else:
                    break

            if right == N:
                return max(max_len, right - left)

            max_len = max(max_len, right - left)

            # Shrink window.
            while curr_window[nums[left]] < k:
                curr_window[nums[left]] -= 1
                left += 1

            curr_window[nums[left]] -= 1
            left += 1

        return max_len


sol = Solution()
print(sol.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
print(sol.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1))
print(sol.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4))
