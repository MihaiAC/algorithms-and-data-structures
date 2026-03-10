from typing import Tuple
from functools import reduce
from collections.abc import Callable
from collections import defaultdict, deque

class Gate:
    def __init__(self, name: str, operation: Callable[[Tuple[bool, bool]], bool]):
        self.inputs = []
        self.operation = operation
        self.name = name


class Solution:
    AND = lambda x,y: x and y
    OR = lambda x,y: x or y
    XOR = lambda x,y: x ^ y
    NOOP = lambda x,y: x

    def __init__(self, input_file: str):
        input_lines = open(input_file).read().strip().split('\n')
        
        self.initial_values = []
        self.input_to = defaultdict(list)
        self.name_to_gate = dict()
        
        parsed_first_half = False
        for line in input_lines:
            if line == '':
                parsed_first_half = True
                continue
            
            if not parsed_first_half:
                register, value = line.split(': ')
                if value == '0':
                    self.initial_values.append((register, False))
                else:
                    self.initial_values.append((register, True))
            else:
                line_vals = line.split(' ')
                v1_name, v2_name, gate_name = line_vals[0], line_vals[2], line_vals[4]
                op_name = line_vals[1]
                
                if op_name == 'XOR':
                    op = Solution.XOR
                elif op_name == 'AND':
                    op = Solution.AND
                else:
                    op = Solution.OR
                
                self.name_to_gate[gate_name] = Gate(gate_name, op)
                self.input_to[v1_name].append(gate_name)
                self.input_to[v2_name].append(gate_name)
    
    def calculate_output(self) -> int:
        zs_to_vals = dict()
        
        queue = deque()
        for (register, val) in self.initial_values:
            queue.appendleft((register, val))
        
        while len(queue) > 0:
            register, val = queue.pop()

            if register[0] == 'z':
                zs_to_vals[register] = int(val)
            
            for gate_name in self.input_to[register]:
                gate = self.name_to_gate[gate_name]
                gate.inputs.append(val)
                if len(gate.inputs) == 2:
                    queue.appendleft((gate_name, reduce(gate.operation, gate.inputs)))

        zs = list(zs_to_vals.keys())
        zs.sort(reverse=True)

        output = 0
        for z in zs:
            output = output*2 + zs_to_vals[z]
        
        return output


if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_output())
