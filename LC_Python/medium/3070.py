from typing import List
from collections import defaultdict


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        dp = defaultdict(int)

        count = 0
        for ii in range(M):
            for jj in range(N):
                dp[(ii, jj)] = (
                    dp[(ii - 1, jj)]
                    + dp[(ii, jj - 1)]
                    - dp[(ii - 1, jj - 1)]
                    + grid[ii][jj]
                )

                if dp[(ii, jj)] <= k:
                    count += 1
                else:
                    break

        return count


# uv run pytest ...
def tests():
    sol = Solution()
    assert sol.countSubmatrices([[7, 6, 3], [6, 6, 1]], 18) == 4
    assert sol.countSubmatrices([[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20) == 6
    assert sol.countSubmatrices([[1, 10], [7, 2], [9, 1], [4, 1]], 8) == 2
