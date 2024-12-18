from collections import deque

class Solution:
    def __init__(self, input_file: str, nbytes: int, nrows: int, ncols: int):
        self.obstacles = set()
        lines = open(input_file).read().strip().split('\n')

        byte_count = 0
        for line in lines:
            if byte_count >= nbytes:
                break
            dx, dy = [int(x) for x in line.split(',')]
            self.obstacles.add((dx, dy))
            byte_count += 1
        
        self.nrows, self.ncols = nrows, ncols
    
    def calculate_shortest_path_len(self) -> int:
        visited = set()
        visited.add((0, 0))

        dist = 0
        queue = deque([(0, 0)])

        while len(queue) > 0:
            for _ in range(len(queue)):
                cx, cy = queue.pop()
                if (cx, cy) == (self.nrows-1, self.ncols-1):
                    return dist
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= cx+dx < self.nrows and 0 <= cy+dy < self.ncols and (cx+dx, cy+dy) not in self.obstacles and (cx+dx, cy+dy) not in visited:
                        visited.add((cx+dx, cy+dy))
                        queue.appendleft((cx+dx, cy+dy))
            dist += 1
        
        return -1

if __name__ == '__main__':
    sol = Solution('input', 3029, 71, 71)
    print(sol.calculate_shortest_path_len())