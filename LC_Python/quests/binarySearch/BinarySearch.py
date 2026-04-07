from typing import List
from bisect import bisect_right


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_right(nums, target)
        return -1 if nums[idx - 1] != target else idx - 1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
