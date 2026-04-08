from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()

        smallest = nums[0] + nums[1] + nums[2]
        if target <= smallest:
            return smallest

        largest = nums[-1] + nums[-2] + nums[-3]
        if largest <= target:
            return largest

        ans = largest if abs(largest - target) < abs(smallest - target) else smallest

        for idx in range(N - 2):
            left, right = idx + 1, N - 1
            while left < right:
                curr_sum = nums[idx] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(ans - target):
                    ans = curr_sum

                if curr_sum == target:
                    return target
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert sol.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert sol.threeSumClosest([0, 0, 0], 1) == 0
