from typing import List
from collections import deque

DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        visited = set()

        def within_bounds(x: int, y: int) -> bool:
            return x >= 0 and y >= 0 and x < M and y < N

        for ii in range(M):
            for jj in range(N):
                if (ii, jj) in visited:
                    continue

                visited.add((ii, jj))
                queue = deque()
                queue.appendleft((ii, jj, None, None))
                while len(queue) > 0:
                    cx, cy, prev_x, prev_y = queue.pop()

                    for dx, dy in DELTAS:
                        nx, ny = cx + dx, cy + dy
                        if within_bounds(nx, ny) and grid[nx][ny] == grid[cx][cy] and (nx, ny) != (prev_x, prev_y):
                            if (nx, ny) in visited:
                                return True

                            visited.add((nx, ny))
                            queue.appendleft((nx, ny, cx, cy))

        return False


sol = Solution()
print(
    sol.containsCycle(
        [
            ["a", "a", "a", "a"],
            ["a", "b", "b", "a"],
            ["a", "b", "b", "a"],
            ["a", "a", "a", "a"],
        ]
    )
)

print(
    sol.containsCycle(
        [
            ["c", "c", "c", "a"],
            ["c", "d", "c", "c"],
            ["c", "c", "e", "c"],
            ["f", "c", "c", "c"],
        ]
    )
)

print(sol.containsCycle([["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))
