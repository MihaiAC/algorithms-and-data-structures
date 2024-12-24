from typing import Tuple, Dict, List
from functools import reduce
from collections.abc import Callable
from collections import defaultdict, deque

class Wire:
    def __init__(self, name: str, value: bool):
        self.name = name
        self.value = value
        self.outputs = []
    
    @property
    def is_wire(self) -> bool:
        return True
    
    @property
    def is_gate(self) -> bool:
        return False

class Gate:
    def __init__(self, name: str, operator_name: str=None, operator_f: Callable[[Tuple[bool, bool]], bool]=None):
        self.name = name
        
        self.inputs = []
        self.outputs = []
        
        self.operator_name = operator_name
        self.operator_f = operator_f
    
    @property
    def value(self):
        if len(self.inputs) != 2:
            raise ValueError('Attempted to calculate the value of a gate with fewer than two inputs.')
        return int(self.operator_f(self.inputs[0].value, self.inputs[1].value))
    
    @property
    def is_wire(self) -> bool:
        return False
    
    @property
    def is_gate(self) -> bool:
        return True
    
    def is_fixed(self) -> bool:
        inp1 = self.inputs[0]
        inp2 = self.inputs[1]

        if inp1.is_wire and inp2.is_wire:
            return True
        elif self.operator_name == 'AND' and ((inp1.value == 0 and (inp1.is_wire or inp1.is_fixed())) or 
                                              (inp2.value == 0 and (inp2.is_wire or inp2.is_fixed()))):
            return True
        elif self.operator_name == 'OR' and ((inp1.value == 1 and (inp1.is_wire or inp1.is_fixed())) or 
                                             (inp2.value == 1 and (inp2.is_wire or inp2.is_fixed()))):
            return True
        elif inp1.is_wire and inp2.is_fixed():
            return True
        elif inp2.is_wire and inp1.is_fixed():
            return True
        elif inp1.is_gate and inp1.is_fixed() and inp2.is_gate and inp2.is_fixed():
            return True
        return False
    

class Solution:
    SELECT_OP = {
        'AND': lambda x,y: x and y,
        'OR' : lambda x,y: x or y,
        'XOR': lambda x,y: x ^ y
    }

    def __init__(self, input_file: str):
        input_lines = open(input_file).read().strip().split('\n')
        
        self.x_wires = dict()
        self.y_wires = dict()
        self.input_to = defaultdict(list)
        self.gates = dict()
        
        parsed_first_half = False
        for line in input_lines:
            if line == '':
                parsed_first_half = True
                continue
            
            if not parsed_first_half:
                wire_name, wire_value = line.split(': ')
                if wire_name[0] == 'x':
                    self.x_wires[wire_name] = Wire(wire_name, int(wire_value))
                else:
                    self.y_wires[wire_name] = Wire(wire_name, int(wire_value))
            else:
                line_vals = line.split(' ')
                v1_name, v2_name, gate_name = line_vals[0], line_vals[2], line_vals[4]
                op_name = line_vals[1]
                
                self.add_gate_by_name(v1_name)
                self.add_gate_by_name(v2_name)
                self.add_gate_by_name(gate_name)
                
                input_1 = self.get_by_name(v1_name)
                input_2 = self.get_by_name(v2_name)
                gate = self.get_by_name(gate_name)
                
                gate.inputs.append(input_1)
                gate.inputs.append(input_2)

                gate.operator_f = Solution.SELECT_OP[op_name]
                gate.operator_name = op_name

                input_1.outputs.append(gate)
                input_2.outputs.append(gate)
        
        # Dict that maps the z_gate name to its desired output.
        # Dict[str, int]
        self.correct_zs = self.calculate_correct_zs()

        # Gates whose output cannot be changed by switching one input.
        self.fixed_gates = self.calculate_fixed_gates()
        print(x.name for x in self.fixed_gates)
    
    def is_wire(self, name: str) -> bool:
        return name[0] in ['x', 'y']

    def get_by_name(self, name: str) -> Wire | Gate:
        if name[0] == 'x':
            return self.x_wires[name]
        elif name[0] == 'y':
            return self.y_wires[name]
        return self.gates[name]

    def add_gate_by_name(self, name: str):
        # Check if the variable name refers to a wire.
        if self.is_wire(name):
            return

        # Check if we have already added this gate.
        if name in self.gates:
            return
        
        # Add a new gate with the provided name as ID.
        new_gate = Gate(name)
        self.gates[name] = new_gate

        return
        

    def calculate_correct_zs(self) -> Dict[str, int]:
        x_keys = sorted(list(self.x_wires.keys()))
        y_keys = sorted(list(self.y_wires.keys()))
        carry = 0

        correct_zs = dict()
        for idx in range(len(x_keys)):
            x_key, y_key = x_keys[idx], y_keys[idx]
            x_val, y_val = self.x_wires[x_key].value, self.y_wires[y_key].value
            z_key = 'z' + x_key[1:]

            if x_val == 1 and y_val == 1:
                z_val = carry
                carry = 1
            elif x_val == 1 or y_val == 1:
                z_val = 1-carry
            else:
                z_val = carry
                carry = 0
            
            correct_zs[z_key] = z_val

            # print(f"{x_key}={x_val} {y_key}={y_val} {z_key}={z_val} carry={carry}")
        
        last_z_nr = int(x_key[1:])+1
        if last_z_nr < 10:
            last_z_key = 'z0' + str(last_z_nr)
        else:
            last_z_key = 'z' + str(last_z_nr) 
        
        correct_zs[last_z_key] = carry
        return correct_zs
    
    def calculate_fixed_gates(self) -> List[Gate]:
        return [x for x in self.gates.values() if x.is_fixed()]



if __name__ == '__main__':
    sol = Solution('test1')
    print(sol.calculate_fixed_gates())
