from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        dp = [{} for _ in range(N)]
        dp[0][0] = 0

        for ii in range(M):
            for jj in range(N):
                prev_row = dp[jj].copy()
                curr_cost = 0 if grid[ii][jj] == 0 else 1
                curr_row = {}
                for c in range(k + 1):
                    prev_max = None

                    if c - curr_cost in prev_row:
                        prev_max = prev_row[c - curr_cost]

                    if jj > 0 and c - curr_cost in dp[jj - 1]:
                        if prev_max is None:
                            prev_max = dp[jj - 1][c - curr_cost]
                        else:
                            prev_max = max(prev_max, dp[jj - 1][c - curr_cost])

                    if prev_max is not None:
                        curr_row[c] = grid[ii][jj] + prev_max
                dp[jj] = curr_row

        scores = dp[N - 1].values()
        return -1 if len(scores) == 0 else max(scores)


sol = Solution()
print(sol.maxPathScore([[0, 1], [2, 0]], 1))
print(sol.maxPathScore([[0, 1], [1, 2]], 1))
