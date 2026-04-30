from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        dp = [{} for _ in range(N)]
        # dp[jj][c] = max score for current row, jj col, with c spent
        dp[0][0] = 0

        for ii in range(M):
            for jj in range(N):
                prev_row = dp[jj].copy()
                curr_cost = 0 if grid[ii][jj] == 0 else 1
                curr_row = {}

                left = dp[jj - 1] if jj > 0 else {}
                merged = {
                    prev_cost: max(left.get(prev_cost, -1), prev_row.get(prev_cost, -1))
                    for prev_cost in left.keys() | prev_row.keys()
                }

                if curr_cost == 0:
                    curr_row = merged
                else:
                    for prev_cost, prev_max in merged.items():
                        if prev_cost + 1 <= k:
                            curr_row[prev_cost + 1] = grid[ii][jj] + prev_max

                dp[jj] = curr_row

        scores = dp[N - 1].values()
        return -1 if len(scores) == 0 else max(scores)


sol = Solution()
print(sol.maxPathScore([[0, 1], [2, 0]], 1))
print(sol.maxPathScore([[0, 1], [1, 2]], 1))
