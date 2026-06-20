from typing import List


class Solution:
    def maxBuilding(self, n: int, restrict: List[List[int]]) -> int:
        restrict.append([1, 0])
        restrict.sort()
        if restrict[-1][0] != n:
            restrict.append([n, n - 1])

        # L->R pass
        m = len(restrict)
        for idx in range(1, m):
            restrict[idx][1] = min(
                restrict[idx][1],
                restrict[idx - 1][1] + (restrict[idx][0] - restrict[idx - 1][0]),
            )

        # R->L pass
        for idx in range(m - 2, 0, -1):
            restrict[idx][1] = min(
                restrict[idx][1],
                restrict[idx + 1][1] + (restrict[idx + 1][0] - restrict[idx][0]),
            )

        ans = 0
        for idx in range(m - 1):
            best = (
                (restrict[idx + 1][0] - restrict[idx][0])
                + restrict[idx][1]
                + restrict[idx + 1][1]
            ) // 2
            ans = max(ans, best)

        return ans


sol = Solution()
print(sol.maxBuilding(5, [[2, 1], [4, 1]]))
print(sol.maxBuilding(6, []))
print(sol.maxBuilding(10, [[5, 3], [2, 5], [7, 4], [10, 3]]))
