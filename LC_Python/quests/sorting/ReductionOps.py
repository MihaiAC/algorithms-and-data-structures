from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n_ops = 0
        total = 0
        nums.sort()

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                n_ops += 1
            total += n_ops

        return total


if __name__ == "__main__":
    sol = Solution()
    assert sol.reductionOperations([5, 1, 3]) == 3
    assert sol.reductionOperations([1, 1, 1]) == 0
    assert sol.reductionOperations([1, 1, 2, 2, 3]) == 4
