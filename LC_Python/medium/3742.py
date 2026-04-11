from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        num_to_indices = defaultdict(list)
        maxD = 3 * (len(nums) - 1)
        ans = maxD

        for idx, num in enumerate(nums):
            indices = num_to_indices[num]
            indices.append(idx)

            if len(indices) == 3:
                ans = min(ans, 2 * (idx - indices[0]))
                num_to_indices[num] = indices[1:]

        return ans if ans < maxD else -1


sol = Solution()
print(sol.minimumDistance([1, 2, 1, 1, 3]))
print(sol.minimumDistance([1, 1, 2, 3, 2, 1, 2]))
print(sol.minimumDistance([1]))
