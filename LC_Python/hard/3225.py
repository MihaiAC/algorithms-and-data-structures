from typing import List


class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        N = len(grid)

        dp = [[[0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N)]

        prefix_sum = [[0] * N for _ in range(N + 1)]
        for ii in range(1, N + 1):
            for jj in range(N):
                prefix_sum[ii][jj] = grid[ii - 1][jj] + prefix_sum[ii - 1][jj]

        for col in range(1, N):
            for curr_h in range(N + 1):
                # Can split this if + for into two for to reduce nesting.
                for last_h in range(N + 1):
                    if curr_h <= last_h:
                        curr_max = 0
                        # TODO: This needs to be memoized as well.
                        for penultimate_h in range(N + 1):
                            curr_max = max(curr_max, dp[col - 1][last_h][penultimate_h])
                        dp[col][curr_h][last_h] = (
                            curr_max
                            + prefix_sum[last_h][col]
                            - prefix_sum[curr_h][col]
                        )
                    else:
                        curr_max = 0
                        for penultimate_h in range(N + 1):
                            curr_max = max(
                                curr_max,
                                dp[col - 1][last_h][penultimate_h]
                                + max(
                                    0,
                                    prefix_sum[curr_h][col - 1]
                                    - prefix_sum[max(last_h, penultimate_h)][col - 1],
                                ),
                            )
                        dp[col][curr_h][last_h] = curr_max

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
