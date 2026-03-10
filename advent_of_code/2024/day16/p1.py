import heapq
from typing import Tuple

class Solution:
    def __init__(self, input_file: str):
        self.matrix = open(input_file).read().strip().split('\n')
        self.M = len(self.matrix)
        self.N = len(self.matrix[0])

        self.init_constants()
    
    def init_constants(self):
        self.TO_DELTA = {
            '>': (0, 1),
            '^': (-1, 0),
            'v': (1, 0),
            '<': (0, -1)
        }

        self.DELTAS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        self.TO_SYMBOL = {
            (0, 1): '>',
            (-1, 0): '^',
            (1, 0): 'v',
            (0, -1): '<'
        }

        self.STEP_COST = 1
        self.TURN_COST = 1000
    
    def find_start(self) -> Tuple[int, int]:
        for ii in range(self.M):
            for jj in range(self.N):
                if self.matrix[ii][jj] == 'S':
                    return (ii, jj)

    def calc_min_cost(self) -> int:
        cx, cy = self.find_start()
        visited = set()
        heap = [(0, cx, cy, '>')]
        while len(heap) > 0:
            curr_cost, cx, cy, curr_dir = heapq.heappop(heap)

            if (cx, cy, curr_dir) in visited:
                continue
            
            visited.add((cx, cy, curr_dir))
            
            if self.matrix[cx][cy] == 'E':
                return curr_cost
            
            for (dx, dy) in self.DELTAS:
                nx, ny = cx+dx, cy+dy
                
                if self.matrix[nx][ny] == '#' or (nx, ny, self.TO_SYMBOL[(dx, dy)]) in visited:
                    continue
                
                new_cost = curr_cost + self.STEP_COST
                if self.TO_SYMBOL[(dx, dy)] != curr_dir:
                    new_cost += self.TURN_COST

                heapq.heappush(heap, (new_cost, nx, ny, self.TO_SYMBOL[(dx, dy)]))
        
        return -1
        

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calc_min_cost())