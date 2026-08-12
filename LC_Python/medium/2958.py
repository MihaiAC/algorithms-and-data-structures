from typing import List
from collections import defaultdict, deque


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window = deque()
        curr_window = defaultdict(int)
        max_len = 0

        for num in nums:
            window.append(num)
            curr_window[num] += 1

            while curr_window[num] > k:
                curr_window[window.popleft()] -= 1

            max_len = max(max_len, len(window))

        return max_len


sol = Solution()
print(sol.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
print(sol.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1))
print(sol.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4))
