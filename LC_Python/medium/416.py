from typing import List
from functools import cache


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def max_diff(left_idx: int, right_idx: int) -> int:
            if left_idx == right_idx:
                return nums[left_idx]

            return max(
                nums[left_idx] - max_diff(left_idx + 1, right_idx),
                nums[right_idx] - max_diff(left_idx, right_idx - 1),
            )

        return max_diff(0, len(nums) - 1) >= 0


sol = Solution()
print(sol.PredictTheWinner([1, 5, 2]))
print(sol.PredictTheWinner([1, 5, 233, 7]))
