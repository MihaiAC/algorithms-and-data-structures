from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        prev_row = [{} for _ in range(N)]
        curr_row = [{} for _ in range(N)]
        curr_row[0][0] = 0

        for ii in range(M):
            for jj in range(1, N):
                curr_cost = 0 if grid[ii][jj] == 0 else 1
                for c in range(k + 1):
                    if c < curr_cost and c in curr_row[jj]:
                        del curr_row[jj][c]
                        continue

                    prev_max = None

                    if ii > 0 and c - curr_cost in prev_row[jj]:
                        prev_max = prev_row[jj][c - curr_cost]

                    if jj > 0 and c - curr_cost in curr_row[jj - 1]:
                        if prev_max is None:
                            prev_max = curr_row[jj - 1][c - curr_cost]
                        else:
                            prev_max = max(prev_max, curr_row[jj - 1][c - curr_cost])

                    if prev_max is not None:
                        curr_row[jj][c] = grid[ii][jj] + prev_max
                    elif c in curr_row[jj]:
                        del curr_row[jj][c]

            # Update curr_row[0][0..k].
            if ii < M - 1:
                prev_row, curr_row = curr_row, prev_row
                curr_cost = 0 if grid[ii + 1][0] == 0 else 1
                for c in range(0, k + 1):
                    if c < curr_cost:
                        if c in curr_row[0]:
                            del curr_row[0][c]
                    elif c - curr_cost in prev_row[0]:
                        curr_row[0][c] = prev_row[0][c - curr_cost] + grid[ii + 1][0]
                    elif c in curr_row[0]:
                        del curr_row[0][c]

        scores = curr_row[N - 1].values()
        return -1 if len(scores) == 0 else max(scores)


sol = Solution()
print(sol.maxPathScore([[0, 1], [2, 0]], 1))
print(sol.maxPathScore([[0, 1], [1, 2]], 1))
