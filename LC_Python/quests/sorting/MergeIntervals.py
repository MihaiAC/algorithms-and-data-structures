from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []
        curr_left, curr_right = intervals[0]
        for left, right in intervals[1:]:
            if curr_right < left:
                ans.append([curr_left, curr_right])
                curr_left, curr_right = left, right
            else:
                curr_right = max(curr_right, right)
        ans.append([curr_left, curr_right])

        return ans
