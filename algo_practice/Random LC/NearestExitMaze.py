from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        nrows = len(maze)
        ncols = len(maze[0])

        srow, scol = entrance[0], entrance[1]
        cost = dict()
        queue = deque()

        cost = []
        for _ in range(nrows):
            cost.append([-1]*ncols)
        cost[srow][scol] = 0

        queue.appendleft((srow, scol))

        while len(queue) > 0:
            curr_row, curr_col = queue.pop()
            curr_cost = cost[curr_row][curr_col]
            for row, col in [(curr_row+1, curr_col), (curr_row-1, curr_col), (curr_row, curr_col+1), (curr_row, curr_col-1)]:
                if row < 0 or row >= nrows or col < 0 or col >= ncols:
                    continue
                if maze[row][col] == '+':
                    continue
                if cost[row][col] >= 0:
                    continue
                if row == 0 or row == nrows-1 or col == 0 or col == ncols-1:
                    return curr_cost+1
                cost[row][col] = curr_cost+1
                queue.appendleft((row, col))
        
        return -1

if __name__ == '__main__':
    sol = Solution()
    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance = [1,0]
    print(sol.nearestExit(maze, entrance))
