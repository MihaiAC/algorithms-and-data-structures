from typing import List
from collections import defaultdict


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # convert nums s.t. nums[i] = 1 if == target else -1
        # do prefix sum of this new nums array
        # count[prefix_sum] = how many times we've encountered prefix_sum so far
        count = defaultdict(int)
        count[0] = 1

        # current prefix sum
        prefix_sum = 0

        # the current prefix sum of count that we're interested in
        # equal to the number of valid subarrays that have the current num as their
        # last element
        count_prefix_sum = 0

        ans = 0

        for num in nums:
            if num == target:
                count_prefix_sum += count[prefix_sum]
                prefix_sum += 1
            else:
                prefix_sum -= 1
                count_prefix_sum -= count[prefix_sum]

            count[prefix_sum] += 1
            ans += count_prefix_sum

        return ans


sol = Solution()
print(sol.countMajoritySubarrays([1, 2, 2, 3], 2))
print(sol.countMajoritySubarrays([1, 1, 1, 1], 1))
print(sol.countMajoritySubarrays([1, 2, 3], 4))
