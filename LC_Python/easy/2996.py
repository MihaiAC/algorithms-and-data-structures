from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        idx = 1
        while idx < len(nums):
            if nums[idx] == nums[idx - 1] + 1:
                curr_sum += nums[idx]
                idx += 1
            else:
                break

        rest_set = set(nums[(idx - 1) :])
        while curr_sum in rest_set:
            curr_sum += 1

        return curr_sum


sol = Solution()
print(sol.missingInteger([1, 2, 3, 2, 5]))
print(sol.missingInteger([3, 4, 5, 1, 12, 14, 13]))
print(sol.missingInteger([29]))
