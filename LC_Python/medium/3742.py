from typing import List

MINUS_INF = float("-inf")


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        prev_row = [[MINUS_INF] * (k + 1) for _ in range(N)]
        curr_row = [[MINUS_INF] * (k + 1) for _ in range(N)]
        curr_row[0][0] = 0

        for ii in range(M):
            for jj in range(1, N):
                curr_cost = 0 if grid[ii][jj] == 0 else 1
                for c in range(k + 1):
                    if c < curr_cost:
                        curr_row[jj][c] = MINUS_INF
                        continue

                    prev_max = MINUS_INF

                    if ii > 0:
                        prev_max = max(prev_max, prev_row[jj][c - curr_cost])
                    if jj > 0:
                        prev_max = max(prev_max, curr_row[jj - 1][c - curr_cost])

                    curr_row[jj][c] = grid[ii][jj] + prev_max

            # Update curr_row[0][0..k].
            if ii < M - 1:
                prev_row, curr_row = curr_row, prev_row
                curr_cost = 0 if grid[ii + 1][0] == 0 else 1
                for c in range(0, k + 1):
                    if c < curr_cost:
                        curr_row[0][c] = MINUS_INF
                    else:
                        curr_row[0][c] = prev_row[0][c - curr_cost] + grid[ii + 1][0]

        ans = max(curr_row[N - 1])
        return -1 if ans == MINUS_INF else ans


sol = Solution()
print(sol.maxPathScore([[0, 1], [2, 0]], 1))
print(sol.maxPathScore([[0, 1], [1, 2]], 1))
