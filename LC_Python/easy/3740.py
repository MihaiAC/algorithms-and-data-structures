from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        ans = 3 * len(nums)

        for idx, num in enumerate(nums):
            indices[num].append(idx)
            if len(indices[num]) >= 3:
                ans = min(ans, 2 * (indices[num][-1] - indices[num][-3]))

        return -1 if ans == 3 * len(nums) else ans


sol = Solution()
print(sol.minimumDistance([1, 2, 1, 1, 3]))
print(sol.minimumDistance([1, 1, 2, 3, 2, 1, 2]))
print(sol.minimumDistance([1]))
