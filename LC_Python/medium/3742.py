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

                if jj > 0:
                    for c, prev_max in dp[jj - 1].items():
                        if c + curr_cost <= k:
                            curr_row[c + curr_cost] = grid[ii][jj] + prev_max

                for c, prev_max in prev_row.items():
                    if c + curr_cost <= k:
                        curr_row[c + curr_cost] = max(
                            grid[ii][jj] + prev_max, curr_row.get(c + curr_cost, -1)
                        )

                dp[jj] = curr_row

        scores = dp[N - 1].values()
        return -1 if len(scores) == 0 else max(scores)


sol = Solution()
print(sol.maxPathScore([[0, 1], [2, 0]], 1))
print(sol.maxPathScore([[0, 1], [1, 2]], 1))
