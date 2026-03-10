from collections import defaultdict
from typing import List
from copy import deepcopy

import networkx as nx

class Solution:
    def __init__(self, input_file: str):
        lines = open(input_file).read().strip().split('\n')
        
        self.graph = nx.Graph()
        for line in lines:
            u, v = line.split('-')
            self.graph.add_edge(u, v) 

    def find_max_len_clique(self) -> str:
        longest_clique = list(nx.approximation.max_clique(self.graph))
        longest_clique.sort()
        return ",".join(longest_clique)

        
if __name__ == '__main__':
    sol = Solution('input')
    print(sol.find_max_len_clique())

        