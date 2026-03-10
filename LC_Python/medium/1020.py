from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])

        queue = deque()

        if nrows == 1 or ncols == 1:
            return 0

        for x in range(nrows):
            if grid[x][0] == 1:
                queue.append((x, 0))
                grid[x][0] = 0
            
            if grid[x][ncols-1] == 1:
                queue.append((x, ncols-1))
                grid[x][ncols-1] = 0
            
        for y in range(ncols):
            if grid[0][y] == 1:
                queue.append((0, y))
                grid[0][y] = 0
            
            if grid[nrows-1][y] == 1:
                queue.append((nrows-1, y))
                grid[nrows-1][y] = 0

        while len(queue) > 0:
            for _ in range(len(queue)):
                nx, ny = queue.popleft()
                for cx, cy in [(nx+1, ny), (nx-1, ny), (nx, ny+1), (nx, ny-1)]:
                    if cx == -1 or cx == nrows or cy == -1 or cy == ncols:
                        continue
                    
                    if grid[cx][cy] == 0:
                        continue
                    
                    queue.append((cx, cy))
                    grid[cx][cy] = 0
        
        nr_enclaves = 0
        for x in range(1, nrows-1):
            for y in range(1, ncols-1):
                nr_enclaves += grid[x][y]
        
        return nr_enclaves