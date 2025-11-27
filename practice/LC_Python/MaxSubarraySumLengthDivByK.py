from typing import List
from math import inf


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_prefix_sum = [inf] * k
        min_prefix_sum[0] = 0

        curr_sum = 0
        ans = -inf

        for idx in range(1, len(nums) + 1):
            curr_sum += nums[idx - 1]

            ans = max(ans, curr_sum - min_prefix_sum[idx % k])

            if min_prefix_sum[idx % k] > curr_sum:
                min_prefix_sum[idx % k] = curr_sum

        return ans
