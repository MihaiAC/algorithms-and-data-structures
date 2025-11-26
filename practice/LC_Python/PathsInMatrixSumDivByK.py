from typing import List

MODN = 10**9 + 7


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])

        dp = [[0] * k for _ in range(N)]
        dp[0][grid[0][0] % k] = 1

        for jj in range(1, N):
            num = grid[0][jj] % k
            for rest in range(k):
                prev_rest = (rest - num + k) % k
                dp[jj][rest] = dp[jj - 1][prev_rest]

        for ii in range(1, M):
            new_dp = [[0] * k for _ in range(N)]

            num = grid[ii][0] % k
            for rest in range(k):
                prev_rest = (rest - num + k) % k
                new_dp[0][rest] = dp[0][prev_rest]

            for jj in range(1, N):
                num = grid[ii][jj] % k
                for rest in range(k):
                    prev_rest = (rest - num + k) % k
                    new_dp[jj][rest] = (
                        dp[jj][prev_rest] + new_dp[jj - 1][prev_rest]
                    ) % MODN

            dp = new_dp

        return dp[N - 1][0]
