import re
import pulp
import numpy as np
from typing import Tuple

class Solution:
    def __init__(self, input_file: str):
        self.equations = []
        self.OFFSET = 10000000000000
        
        pattern = re.compile(r"Button A: X\+([0-9]+), Y\+([0-9]+)\nButton B: X\+([0-9]+), Y\+([0-9]+)\nPrize: X=([0-9]+), Y=([0-9]+)")
        with open(input_file) as f: 
            for match in pattern.findall(f.read()):
                current_equation = [int(x) for x in match]
                current_equation[-1] += self.OFFSET
                current_equation[-2] += self.OFFSET

                self.equations.append(current_equation)
    
    '''
        Let npA = number of pulls of the first lever (A)
            npB = number of pulls of the second lever (B)
        First, solve the system of equations.
            xA * npA + xB * npB = xres
            yA * npA + yB * npB = yres
        
        If the determinant is != 0 => unique solution - check if it is comprised of integers.
        If the determinant is 0 and one of detA, detB is 0 => optimization problem:
        minimize(3*npA + npB) subject to: xA * npA + xB * npB = xres and npA, npB = integers
        Otherwise, there are no solutions.
    '''
    def find_min_tokens(self, equation: Tuple[int, int, int, int, int, int]) -> int:
        xA, yA, xB, yB, xres, yres = equation
        
        # Calculate determinant.
        det = xA*yB-xB*yA
        detA = xres*yB-yres*xB
        detB = xA*yres-yA*xres
        if det != 0:
            if detA % det == 0 and detB % det == 0:
                return 3*(detA//det) + (detB//det)
            else:
                return 0
        elif detA == 0 or detB == 0:
            optimization_problem = pulp.LpProblem("Minimize cost", pulp.LpMinimize)
            npA = pulp.LpVariable("npA", lowBound=0, cat="Integer")
            npB = pulp.LpVariable("npB", lowBound=0, cat="Integer")

            optimization_problem += 3*npA + npB, "Minimization objective"
            optimization_problem += yA * npA + yB * npB == yres, "Linear constraint"

            optimization_problem.solve()

            if optimization_problem.status == pulp.LpStatusOptimal:
                return 3*int(pulp.value(npA)) + int(pulp.value(npB))
            else:
                print("No feasible solution found.")
                return 0
        else:
            # System has no solution.
            return 0
    
    def calculate_min_tokens_needed(self) -> int:
        tokens = 0
        for equation in self.equations:
            tokens += self.find_min_tokens(equation)
        return tokens

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_min_tokens_needed())
