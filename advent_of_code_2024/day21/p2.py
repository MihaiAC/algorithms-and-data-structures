from typing import Dict, Tuple, List
from collections import defaultdict

class Solution:
    def __init__(self, input_file: str):
        self.init_constants()
        self.inputs = open(input_file).read().strip().split('\n')
        
        self.NUMPAD_SCHEMA = self.precompute_shortest_route(self.NUMPAD, self.NUMPAD_AVOID)
        self.DIRECTIONAL_SCHEMA = self.precompute_shortest_route(self.DIRECTIONAL, self.DIRECTIONAL_AVOID)
        # self.DIRECTIONAL_SCHEMA[('A', 'v')] = ['v<A']
    
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


    def precompute_shortest_route(self, matrix: List[List[str]], avoid: Tuple[int, int]) -> Dict[Tuple[str, str], str]:
        M, N = len(matrix), len(matrix[0])
        routes = dict()

        move_alongside_row = lambda delta: self.DELTA_TO_SYM[(0, self.SIGN(delta))] * abs(delta)
        move_alongside_col = lambda delta: self.DELTA_TO_SYM[(self.SIGN(delta), 0)] * abs(delta)

        for ii in range(M):
            for jj in range(N):
                if matrix[ii][jj] == '#':
                    continue
                for kk in range(M):
                    for ll in range(N):
                        if matrix[kk][ll] == '#':
                            continue

                        if (ii, jj) == (kk, ll):
                            routes[(matrix[ii][jj], matrix[ii][jj])] = 'A'
                            continue
                        
                        route = ''

                        dx = kk - ii
                        dy = ll - jj

                        if dx == 0 or dy == 0:
                            route = self.DELTA_TO_SYM[(self.SIGN(dx), 0)] * abs(dx) + self.DELTA_TO_SYM[(0, self.SIGN(dy))] * abs(dy) + 'A'
                        else:
                            # Some shortcut rules.
                            if (ii, ll) != avoid and (kk, jj) != avoid:
                                if ll < jj:
                                    # move alongside row first, then alongside column
                                    route = move_alongside_row(dy) + move_alongside_col(dx) + 'A'
                                elif kk > ii:
                                    # move down the column then right
                                    route = move_alongside_col(dx) + move_alongside_row(dy) + 'A'
                                else:
                                    # order doesn't matter (?) or I haven't figured out a rule for this yet
                                    route = move_alongside_col(dx) + move_alongside_row(dy) + 'A'
                                    # curr_combos.append(move_alongside_row(dy) + move_alongside_col(dx) + 'A')   
                            elif (ii, ll) != avoid:
                                route = move_alongside_row(dy) + move_alongside_col(dx) + 'A'
                            elif (kk, jj) != avoid:
                                route = move_alongside_col(dx) + move_alongside_row(dy) + 'A'
                        
                        routes[(matrix[ii][jj], matrix[kk][ll])] = route
        
        return routes
    
    def expand_code(self, combo_schema: Dict[Tuple[str, str], str], code: str) -> str:
        code = 'A' + code
        new_code = []
        for idx in range(len(code)-1):
            transition = (code[idx], code[idx+1])
            new_code.append(combo_schema[transition])
        return "".join(new_code)
    
    def calculate_final_code_len(self, code: str, repeats: int) -> int:
        code = self.expand_code(self.NUMPAD_SCHEMA, code)
        for _ in range(repeats):
            code = self.expand_code(self.DIRECTIONAL_SCHEMA, code)
        return len(code)

    def calculate_complexity(self, repeats: int) -> int:
        complexity = 0
        for code in self.inputs:
            x = int(code[:-1])
            y = self.calculate_final_code_len(code, repeats)
            complexity += x * y
        return complexity
    
if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_complexity(25))
    # print(sol.NUMPAD_SHORTEST_COMBOS)
    # print(sol.NUMPAD_SHORTEST_COMBOS['2', '7'])
    # print(sol.NUMPAD_SHORTEST_COMBOS['5', '1'])
    # print(sol.NUMPAD_SHORTEST_COMBOS['5', '3'])
    # print(sol.NUMPAD_SHORTEST_COMBOS['5', '9'])
    
    # print(sol.DIRECTIONAL_SHORTEST_COMBOS['A', 'v'])
    

