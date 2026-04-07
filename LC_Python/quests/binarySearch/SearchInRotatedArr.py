from bisect import bisect_right
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        # Special case: array is not rotated.
        if nums[0] < nums[-1]:
            idx = bisect_right(nums, target)
            return -1 if nums[idx - 1] != target else idx - 1

        # Find inflection point.
        def find_inflection() -> int:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] > nums[left]:
                    left = mid
                else:
                    right = mid - 1
            return left

        inflection_idx = find_inflection()
        if target == nums[inflection_idx]:
            return inflection_idx
        elif target >= nums[0]:
            idx = bisect_right(nums, target, hi=inflection_idx)
            return -1 if nums[idx - 1] != target else idx - 1
        else:
            idx = bisect_right(nums, target, lo=inflection_idx + 1)
            return -1 if nums[idx - 1] != target else idx - 1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    assert sol.search([8, 9, 2, 3, 4], 9) == 1
