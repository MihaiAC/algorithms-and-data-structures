from typing import Tuple, Dict, List
from functools import reduce
from collections.abc import Callable
from collections import defaultdict, deque
import pygraphviz as pgv

class Solution:
    def __init__(self, input_file: str):
        input_lines = open(input_file).read().strip().split('\n')
        self.G = pgv.AGraph(directed=True)
        
        op_counter = 0
        parsed_first_half = False
        for line in input_lines:
            if line == '':
                parsed_first_half = True
                continue
            
            if not parsed_first_half:
                wire_name, wire_value = line.split(': ')
                self.G.add_node(wire_name)
            else:
                line_vals = line.split(' ')
                v1_name, v2_name, gate_name = line_vals[0], line_vals[2], line_vals[4]
                op_name = line_vals[1] + str(op_counter)
                op_counter += 1
                
                self.G.add_edge(v1_name, op_name)
                self.G.add_edge(v2_name, op_name)
                self.G.add_edge(op_name, gate_name)
        
        self.G.layout()
        self.G.draw('graph.jpg')

if __name__ == '__main__':
    sol = Solution('input')
