from typing import List

DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        M, N = len(grid), len(grid[0])
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 0:
                    continue

                for dx, dy in DELTAS:
                    if (
                        0 <= x + dx < M
                        and 0 <= y + dy < N
                        and grid[x + dx][y + dy] == 1
                    ):
                        continue
                    perimeter += 1

        return perimeter
