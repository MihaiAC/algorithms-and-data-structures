from collections import defaultdict
from typing import List
from copy import deepcopy

class Solution:
    def __init__(self, input_file: str):
        lines = open(input_file).read().strip().split('\n')
        
        self.neighbors = defaultdict(set)
        for line in lines:
            u, v = line.split('-')
            self.neighbors[u].add(v)
            self.neighbors[v].add(u)
        
        self.nodes = list(self.neighbors.keys())
        self.available_nodes = set(self.neighbors.keys())        
        self.longest_clique = []
        self.visited = set()
    
    def add_clique_to_visited(self, current_clique: List[str]):
        arr = deepcopy(current_clique)
        arr.sort()
        self.visited.add(tuple(arr))
    
    def clique_in_visited(self, current_clique: List[str]) -> bool:
        arr = deepcopy(current_clique)
        arr.sort()
        return tuple(arr) in self.visited

    def find_all_cliques(self, current_clique: List[str]):
        if len(current_clique) > len(self.longest_clique):
            self.longest_clique = deepcopy(current_clique)
        
        if self.clique_in_visited(current_clique):
            return
        
        print(current_clique)
        for node in self.nodes:
            if node in self.available_nodes:
                connected = True
                # Check that node has a connection to all of the nodes in the current_clique.
                for clique_node in current_clique:
                    if node not in self.neighbors[clique_node]:
                        connected = False
                        break
                
                if connected:
                    current_clique.append(node)
                    self.available_nodes.remove(node)
                    
                    self.find_all_cliques(current_clique)
                    
                    current_clique.pop()
                    self.available_nodes.add(node)
        

    def find_max_len_clique(self) -> str:
        self.find_all_cliques([])
        self.longest_clique.sort()
        return ",".join(self.longest_clique)

        
if __name__ == '__main__':
    sol = Solution('input')
    print(sol.find_max_len_clique())

        