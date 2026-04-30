from typing import List

MINUS_INF = float("-inf")


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[[MINUS_INF] * (k + 1) for _ in range(N)] for _ in range(M)]
        dp[0][0][0] = 0

        for ii in range(M):
            for jj in range(N):
                curr_cost = 0 if grid[ii][jj] == 0 else 1
                for c in range(curr_cost, k + 1):
                    prev_max = MINUS_INF

                    if ii > 0:
                        prev_max = max(prev_max, dp[ii - 1][jj][c - curr_cost])
                    if jj > 0:
                        prev_max = max(prev_max, dp[ii][jj - 1][c - curr_cost])

                    if prev_max != MINUS_INF:
                        dp[ii][jj][c] = grid[ii][jj] + prev_max

        ans = max(dp[M - 1][N - 1])
        return -1 if ans == MINUS_INF else ans


sol = Solution()
print(sol.maxPathScore([[0, 1], [2, 0]], 1))
print(sol.maxPathScore([[0, 1], [1, 2]], 1))
