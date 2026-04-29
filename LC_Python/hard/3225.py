from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        N = len(grid)

        dp = [[[0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N)]

        prefix_sum = [[0] * N for _ in range(N + 1)]
        for ii in range(1, N + 1):
            for jj in range(N):
                prefix_sum[ii][jj] = grid[ii - 1][jj] + prefix_sum[ii - 1][jj]

        suffix_max = [[0] * (N + 1) for _ in range(N + 1)]
        prefix_max = [[0] * (N + 1) for _ in range(N + 1)]

        for col in range(1, N):
            for last_h in range(N + 1):
                suffix_max[last_h][N] = dp[col - 1][last_h][N]
                for penultimate_h in range(N - 1, -1, -1):
                    suffix_max[last_h][penultimate_h] = max(
                        suffix_max[last_h][penultimate_h + 1],
                        dp[col - 1][last_h][penultimate_h],
                    )

            for last_h in range(N + 1):
                prefix_max[last_h][0] = dp[col - 1][last_h][0]
                for penultimate_h in range(1, N + 1):
                    penalty = max(
                        0,
                        prefix_sum[penultimate_h][col - 1]
                        - prefix_sum[last_h][col - 1],
                    )
                    prefix_max[last_h][penultimate_h] = max(
                        prefix_max[last_h][penultimate_h - 1],
                        dp[col - 1][last_h][penultimate_h] - penalty,
                    )

            for curr_h in range(N + 1):
                for last_h in range(curr_h, N + 1):
                    dp[col][curr_h][last_h] = (
                        suffix_max[last_h][0]
                        + prefix_sum[last_h][col]
                        - prefix_sum[curr_h][col]
                    )

                for last_h in range(curr_h):
                    extra_score = (
                        prefix_sum[curr_h][col - 1] - prefix_sum[last_h][col - 1]
                    )
                    dp[col][curr_h][last_h] = max(
                        suffix_max[last_h][curr_h],
                        prefix_max[last_h][curr_h] + extra_score,
                    )

        ans = 0
        for penultimate_h in range(N + 1):
            ans = max(ans, dp[N - 1][N][penultimate_h], dp[N - 1][0][penultimate_h])

        return ans


sol = Solution()
print(
    sol.maximumScore(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0],
            [0, 1, 0, 0, 0],
            [5, 0, 0, 3, 0],
            [0, 0, 0, 0, 2],
        ]
    )
)
print(
    sol.maximumScore(
        [
            [10, 9, 0, 0, 15],
            [7, 1, 0, 8, 0],
            [5, 20, 0, 11, 0],
            [0, 0, 0, 1, 2],
            [8, 12, 1, 10, 3],
        ]
    )
)
