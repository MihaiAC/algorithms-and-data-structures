from collections import deque
from typing import Tuple

class Solution:
    def __init__(self, input_file: str):
        with open(input_file) as f:
            self.matrix = f.read().strip().split('\n')
        self.M, self.N = len(self.matrix), len(self.matrix[0])

        self.DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.WINDOWS = [
            [(-1, 0), (0, 1), (-1, 1)],
            [(0, 1), (1, 0), (1, 1)],
            [(1, 0), (0, -1), (1, -1)],
            [(-1, 0), (0, -1), (-1, -1)]
        ]
    
    def within_bounds(self, coord_x: int, coord_y: int) -> bool:
        return 0 <= coord_x < self.M and 0 <= coord_y < self.N

    def count_corners(self, coords: Tuple[int, int]) -> int:
        cx, cy = coords
        corner_count = 0
        current_letter = self.matrix[cx][cy]
        for window in self.WINDOWS:
            same_letter_count = 0
            out_of_bounds_count = 0
            for dx, dy in window[:2]:
                if not self.within_bounds(cx+dx, cy+dy):
                    out_of_bounds_count += 1
                elif self.matrix[cx+dx][cy+dy] == current_letter:
                    same_letter_count += 1
            
            if same_letter_count == 2:
                dx, dy = window[2]
                if self.matrix[cx+dx][cy+dy] != current_letter:
                    corner_count += 1
            elif same_letter_count == 0 and out_of_bounds_count in [0, 1]:
                corner_count += 1
            elif out_of_bounds_count == 2:
                corner_count += 1

        return corner_count    

    def calculate_price(self) -> int:
        total_price = 0
        visited = [[0 for _ in range(self.N)] for _ in range(self.M)]

        for ii in range(self.M):
            for jj in range(self.N):
                if visited[ii][jj] == 0:
                    visited[ii][jj] = 1
                    
                    current_letter = self.matrix[ii][jj]
                    current_sides = 0
                    current_area = 0
                    
                    queue = deque([(ii, jj)])

                    # BFS.
                    while len(queue) > 0:
                        cx, cy = queue.pop()
                        current_area += 1
                        
                        # Number of sides = number of corners.
                        current_sides += self.count_corners((cx, cy))
                        
                        for dx, dy in self.DELTAS:
                            if self.within_bounds(cx+dx, cy+dy) and self.matrix[cx+dx][cy+dy] == current_letter and visited[cx+dx][cy+dy] == 0:
                                visited[cx+dx][cy+dy] = 1
                                queue.appendleft((cx+dx, cy+dy))
                    
                    total_price += current_area * current_sides        
        
        return total_price


if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_price())