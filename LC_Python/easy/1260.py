from typing import List
from collections import deque


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        flattened = deque()

        for ii in range(M):
            for jj in range(N):
                flattened.append(grid[ii][jj])

        for _ in range(k):
            flattened.appendleft(flattened.pop())

        for ii in range(M):
            for jj in range(N):
                grid[ii][jj] = flattened.popleft()

        return grid


sol = Solution()
print(sol.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(sol.shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
print(sol.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9))
