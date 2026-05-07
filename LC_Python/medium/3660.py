from typing import List


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        components = []

        for ii in range(N):
            max_val, left = nums[ii], ii

            while len(components) > 0 and nums[ii] < components[-1][0]:
                val, left = components.pop()
                max_val = max(max_val, val)

            components.append((max_val, left))

        right = N
        while len(components) > 0:
            val, left = components.pop()
            for ii in range(left, right):
                ans[ii] = val
            right = left

        return ans


sol = Solution()
print(sol.maxValue([2, 1, 3]))
print(sol.maxValue([2, 3, 1]))
