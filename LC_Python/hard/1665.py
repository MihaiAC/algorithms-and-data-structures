from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1] - x[0], x[1]))
        curr_min = 0
        rolling_sum = 0

        for actual, start in tasks[::-1]:
            curr_min = max(curr_min, start + rolling_sum)
            rolling_sum += actual

        return curr_min


sol = Solution()
print(sol.minimumEffort([[1, 2], [2, 4], [4, 8]]))
print(sol.minimumEffort([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))
print(sol.minimumEffort([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]))
