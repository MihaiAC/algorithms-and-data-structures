from collections import defaultdict, deque
from typing import List
from copy import deepcopy

class Solution:
    def __init__(self, input_file: str):
        lines = open(input_file).read().strip().split('\n')
        
        self.neighbors = defaultdict(list)
        for line in lines:
            u, v = line.split('-')
            self.neighbors[u].append(v)
            self.neighbors[v].append(u)

        self.cycles = set()
    
    def add_cycle(self, cycle: List[str]):
        cycle.sort()
        self.cycles.add(tuple(cycle))
    
    def calculate_nr_cycles_of_len(self, cycle_length: int) -> int:
        for node in self.neighbors:
            if node[0] != 't':
                continue
            
            queue = deque()
            queue.appendleft([node])
            while len(queue) > 0:
                for _ in range(len(queue)):
                    curr_path = queue.pop()
                    for neighbor in self.neighbors[curr_path[-1]]:
                        if neighbor in curr_path:
                            if neighbor == curr_path[0] and len(curr_path) == cycle_length:
                                self.add_cycle(curr_path)
                        else:
                            if len(curr_path) == cycle_length:
                                continue
                            new_path = deepcopy(curr_path)
                            new_path.append(neighbor)
                            queue.appendleft(new_path)
        return len(self.cycles)
        
if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_nr_cycles_of_len(3))

        