from typing import List
from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)

        intervals = [(intervals[idx][0], intervals[idx][1], idx) for idx in range(N)]
        intervals.sort(key=lambda x: x[0])

        ans = [-1] * N
        for _, end, orig_idx in intervals:
            sorted_idx = bisect_left(intervals, end, key=lambda x: x[0])
            if sorted_idx != N:
                ans[orig_idx] = intervals[sorted_idx][2]

        return ans


sol = Solution()
print(sol.findRightInterval([[1, 2]]))
print(sol.findRightInterval([[3, 4], [2, 3], [1, 2]]))
print(sol.findRightInterval([[1, 4], [2, 3], [3, 4]]))
