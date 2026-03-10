from typing import List
import heapq
from collections import defaultdict


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums) // 3

        min_sums_left = defaultdict(int)
        min_elems_left = []
        sum_so_far = 0
        for idx in range(N):
            sum_so_far += nums[idx]
            heapq.heappush(min_elems_left, -nums[idx])
        min_sums_left[N] = sum_so_far

        for idx in range(N, 2*N):
            if -nums[idx] > min_elems_left[0]:
                sum_so_far += min_elems_left[0] + nums[idx]
                heapq.heappushpop(min_elems_left, -nums[idx])
            min_sums_left[idx+1] = sum_so_far

        max_sums_right = defaultdict(int)
        max_elems_right = []
        sum_so_far = 0
        for idx in range(3*N-1, 2*N-1, -1):
            sum_so_far += nums[idx]
            heapq.heappush(max_elems_right, nums[idx])
        max_sums_right[2*N] = sum_so_far

        for idx in range(2*N-1, N-1, -1):
            if nums[idx] > max_elems_right[0]:
                sum_so_far += nums[idx] - max_elems_right[0]
                heapq.heappushpop(max_elems_right, nums[idx])
            max_sums_right[idx] = sum_so_far

        ans = float("inf")
        for idx in range(N, 2*N+1):
            ans = min(ans, min_sums_left[idx] - max_sums_right[idx])

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 1, 2]
    print(sol.minimumDifference(nums))
