import re
import scipy
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
            min_objective_func = lambda x: 3*x[0] + x[1]
            integer_constraint_func = lambda x: sum([(val-int(val))**2 for val in x])
            linear_constraint = scipy.optimize.LinearConstraint(A=np.array([xA, xB]), lb=xres, ub=xres)
            nonlinear_constraint = scipy.optimize.NonlinearConstraint(fun=integer_constraint_func, lb=1, ub=1)
            bounds = scipy.optimize.Bounds(lb=0)
            res = scipy.optimize.minimize(min_objective_func, np.array([0, 0]), bounds=bounds, 
                                                                                constraints=[linear_constraint, nonlinear_constraint],
                                                                                options={'maxiter': 100})
            
            print(res)
            return 0
        else:
            return 0
    
    def calculate_min_tokens_needed(self) -> int:
        tokens = 0
        for equation in self.equations:
            tokens += self.find_min_tokens(equation)
        return tokens

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_min_tokens_needed())
