from collections import deque
from typing import Tuple, Set

class Solution:
    def __init__(self, input_file: str, nrows: int, ncols: int):
        self.obstacles = []
        lines = open(input_file).read().strip().split('\n')

        for line in lines:
            dx, dy = [int(x) for x in line.split(',')]
            self.obstacles.append((dx, dy))
        
        self.nrows, self.ncols = nrows, ncols
    
    def reachable(self, obstacles: Set[int]) -> bool:
        visited = set()
        visited.add((0, 0))
        queue = deque([(0, 0)])

        while len(queue) > 0:
            for _ in range(len(queue)):
                cx, cy = queue.pop()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= cx+dx < self.nrows and 0 <= cy+dy < self.ncols and (cx+dx, cy+dy) not in obstacles and (cx+dx, cy+dy) not in visited:
                        if (cx+dx, cy+dy) == (self.nrows-1, self.ncols-1):
                            return True
                        visited.add((cx+dx, cy+dy))
                        queue.appendleft((cx+dx, cy+dy))
        
        return False

    def get_first_blocking_byte(self) -> Tuple[int, int]:
        min_byte_idx = 0
        max_byte_idx = len(self.obstacles)-1
        while min_byte_idx < max_byte_idx:
            cutoff_byte_idx = (min_byte_idx + max_byte_idx) // 2
            if self.reachable(set(self.obstacles[:(cutoff_byte_idx+1)])):
                min_byte_idx = cutoff_byte_idx+1
            else:
                max_byte_idx = cutoff_byte_idx
        return self.obstacles[min_byte_idx]

if __name__ == '__main__':
    sol = Solution('input', 71, 71)
    print(sol.get_first_blocking_byte())