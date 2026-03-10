from typing import List
from functools import cache

# Directions are: 0-NE, 1-SE, 2-SW, 3-NW
deltas = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
next_direction = [1, 2, 3, 0]

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        @cache
        def max_diagonal(x: int, y: int, direction: int, start: int, turns_left: int) -> int:
            if x == M or x < 0 or y == N or y < 0:
                return 0
            
            if grid[x][y] != start:
                return 0
            
            dx, dy = deltas[direction]

            curr = 1 + max_diagonal(x+dx, y+dy, direction, 2-start, turns_left)
            if turns_left == 1:
                dx, dy = deltas[next_direction[direction]]
                curr = max(curr, 1 + max_diagonal(x+dx, y+dy, next_direction[direction], 2-start, 0))
            return curr
            

        ans = 0
        for ii in range(M):
            for jj in range(N):
                if grid[ii][jj] == 1:
                    for direction in range(4):
                        dx, dy = deltas[direction]
                        ans = max(ans, 1+max_diagonal(ii+dx, jj+dy, direction, 2, 1))
        return ans