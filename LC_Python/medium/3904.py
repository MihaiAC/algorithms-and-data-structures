from typing import List


class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        N = len(nums)

        suffix_min = [0] * N
        suffix_min[-1] = nums[-1]
        for idx in range(N - 2, -1, -1):
            suffix_min[idx] = min(nums[idx], suffix_min[idx + 1])

        curr_max = -1
        for idx in range(N):
            curr_max = max(curr_max, nums[idx])
            if curr_max - suffix_min[idx] <= k:
                return idx

        return -1


sol = Solution()
print(sol.firstStableIndex([5, 0, 1, 4], 3))
print(sol.firstStableIndex([3, 2, 1], 1))
print(sol.firstStableIndex([0], 0))
