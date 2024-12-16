import heapq
from typing import Tuple
from collections import defaultdict, deque

class Solution:
    def __init__(self, input_file: str):
        self.matrix = open(input_file).read().strip().split('\n')
        self.matrix = [list(x) for x in self.matrix]
        self.M = len(self.matrix)
        self.N = len(self.matrix[0])
        self.DELTAS = {(-1, 0): [(0, 1), (0, -1), (-1, 0)], 
                       (0, -1): [(1, 0), (-1, 0), (0, -1)], 
                       (0, 1): [(1, 0), (-1, 0), (0, 1)], 
                       (1, 0): [(0, 1), (0, -1), (1, 0)]}
    
    def find_start(self) -> Tuple[int, int]:
        for ii in range(self.M):
            for jj in range(self.N):
                if self.matrix[ii][jj] == 'S':
                    return (ii, jj)

    def calc_n_tiles(self) -> int:
        sx, sy = self.find_start()
        
        back = defaultdict(list)
        cost = defaultdict(int)
        visited = set()
        
        heap = [(0, sx, sy, (0, 1), None)]
        
        fx, fy = -1, -1
        min_fin_cost = float('inf')
        while len(heap) > 0:
            curr_cost, cx, cy, curr_delta, prev = heapq.heappop(heap)

            if curr_cost > min_fin_cost:
                break

            if (cx, cy, curr_delta) in visited:
                if curr_cost == cost[(cx, cy, curr_delta)]:
                    back[(cx, cy, curr_delta)].append(prev)
                    continue
            
            visited.add((cx, cy, curr_delta))
            
            if self.matrix[cx][cy] == 'E':
                fx, fy = cx, cy
                min_fin_cost = curr_cost

                # Always add back-edge from last node.
                back[(cx, cy, curr_delta)].append(prev)
                cost[(cx, cy, curr_delta)] = curr_cost
                
                continue
            
            added_back = False
            for (dx, dy) in self.DELTAS[curr_delta]:
                nx, ny = cx+dx, cy+dy
                
                if self.matrix[nx][ny] == '#' or (nx, ny, (dx, dy)) in visited:
                    continue
                
                # Add back-edge only if it's part of a min-dist path.
                if not added_back:
                    added_back = True
                    back[(cx, cy, curr_delta)].append(prev)
                    cost[(cx, cy, curr_delta)] = curr_cost
                
                new_cost = curr_cost + 1
                if (dx, dy) != curr_delta:
                    new_cost += 1000

                heapq.heappush(heap, (new_cost, nx, ny, (dx, dy), (cx, cy, curr_delta)))
        
        print(min_fin_cost)

        visited = set()
        counted = set()
        queue = deque()
        for delta in self.DELTAS.keys():
            if cost[(fx, fy, delta)] == min_fin_cost:
                queue.appendleft((fx, fy, delta))
                visited.add((fx, fy, delta))

        while len(queue) > 0:
            cx, cy, delta = queue.pop()
            self.matrix[cx][cy] = 'O'
            counted.add((cx, cy))
            
            if (cx, cy) == (sx, sy):
                continue
            
            for nx, ny, ndelta in back[(cx, cy, delta)]:
                if (nx, ny, ndelta) not in visited:
                    visited.add((nx, ny, ndelta))
                    queue.appendleft((nx, ny, ndelta))
        
        open('output', 'a+').write('\n'.join(["".join(x) for x in self.matrix]))
        return len(counted)
        

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calc_n_tiles())
