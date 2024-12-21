from typing import Dict, Tuple, List
from collections import defaultdict

class Solution:
    def __init__(self, input_file: str):
        self.init_constants()
        self.inputs = open(input_file).read().strip().split('\n')
        self.NUMPAD_SHORTEST_COMBOS = self.precompute_shortest_combos(self.NUMPAD, self.NUMPAD_AVOID)
        self.DIRECTIONAL_SHORTEST_COMBOS = self.precompute_shortest_combos(self.DIRECTIONAL, self.DIRECTIONAL_AVOID)
    
    def init_constants(self):
        self.DELTA_TO_SYM = {
            (-1, 0): '^',
            (1, 0): 'v',
            (0, 1): '>',
            (0, -1): '<',
            (0, 0): ''
        }
        self.SIGN = lambda x: 0 if x == 0 else 1 if x > 0 else -1
        
        self.NUMPAD = [['7', '8', '9'],
                       ['4', '5', '6'],
                       ['1', '2', '3'],
                       ['#', '0', 'A']]
        self.NUMPAD_AVOID = (3, 0)

        self.DIRECTIONAL = [['#', '^', 'A'],
                            ['<', 'v', '>']]
        self.DIRECTIONAL_AVOID = (0, 0)


    def precompute_shortest_combos(self, matrix: List[List[str]], avoid: Tuple[int, int]) -> Dict[Tuple[str, str], List[str]]:
        M, N = len(matrix), len(matrix[0])
        combos = dict()

        for ii in range(M):
            for jj in range(N):
                if matrix[ii][jj] == '#':
                    continue
                for kk in range(M):
                    for ll in range(N):
                        if matrix[kk][ll] == '#':
                            continue

                        if (ii, jj) == (kk, ll):
                            combos[(matrix[ii][jj], matrix[ii][jj])] = ['A']
                            continue
                        
                        curr_combos = []

                        dx = kk - ii
                        dy = ll - jj

                        if dx == 0 or dy == 0:
                            curr_combos.append(self.DELTA_TO_SYM[(self.SIGN(dx), 0)] * abs(dx) + self.DELTA_TO_SYM[(0, self.SIGN(dy))] * abs(dy) + 'A')
                        else:
                            if (ii, ll) != avoid:
                                # dy first then dx, moving from (ii, jj) to (kk, ll)
                                curr_combos.append(self.DELTA_TO_SYM[(0, self.SIGN(dy))] * abs(dy) + self.DELTA_TO_SYM[(self.SIGN(dx), 0)] * abs(dx) + 'A')


                            if (kk, jj) != avoid:
                                # dx first then dy, moving from (ii, jj) to (kk, ll)
                                curr_combos.append(self.DELTA_TO_SYM[(self.SIGN(dx), 0)] * abs(dx) + self.DELTA_TO_SYM[(0, self.SIGN(dy))] * abs(dy) + 'A')
                        
                        combos[(matrix[ii][jj], matrix[kk][ll])] = curr_combos
        
        return combos
    
    # TODO: improve code by dynamically calculating min_len?
    def code_to_minimal_length_combos(self, combo_schema: Dict[Tuple[str, str], List[str]], equivalent_codes: List[str]) -> List[str]:
        final_combos = []
        for code in equivalent_codes:
            code = 'A' + code
            curr_combos = ['']
            for idx in range(len(code)-1):
                new_combos = []
                transition = (code[idx], code[idx+1])
                for combo in curr_combos:
                    for minimal_combo in combo_schema[transition]:
                        new_combos.append(combo + minimal_combo)
                curr_combos = new_combos
            final_combos += curr_combos
        
        min_len = min([len(x) for x in final_combos])
        return [x for x in final_combos if len(x) == min_len]
    
    def get_final_combos(self, code: str) -> List[str]:
        first_robot_codes = self.code_to_minimal_length_combos(self.NUMPAD_SHORTEST_COMBOS, [code])
        print(len(first_robot_codes))
        second_robot_codes = self.code_to_minimal_length_combos(self.DIRECTIONAL_SHORTEST_COMBOS, first_robot_codes)
        print(len(second_robot_codes))
        third_codes = self.code_to_minimal_length_combos(self.DIRECTIONAL_SHORTEST_COMBOS, second_robot_codes)
        print(len(third_codes))
        return third_codes

    def calculate_complexity(self) -> int:
        complexity = 0
        for code in self.inputs:
            x = int(code[:-1])
            y = len(self.get_final_combos(code)[0])
            complexity += x * y
        return complexity
    
if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_complexity())
    
