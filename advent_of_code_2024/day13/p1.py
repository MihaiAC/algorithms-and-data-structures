import re
from typing import Tuple

class Solution:
    def __init__(self, input_file: str):
        self.equations = []
        
        pattern = re.compile(r"Button A: X\+([0-9]+), Y\+([0-9]+)\nButton B: X\+([0-9]+), Y\+([0-9]+)\nPrize: X=([0-9]+), Y=([0-9]+)")
        with open(input_file) as f: 
            for match in pattern.findall(f.read()):
                current_equation = [int(x) for x in match]
                self.equations.append(current_equation)
    
    '''
        Let npA = number of pulls of the first lever (A)
            npB = number of pulls of the second lever (B)
        We must solve the following optimization problem:
            minimize(3*npA + npB) subject to the constraints:
            npA <= 100
            npB <= 100
            xA * npA + xB * npB = xres
            yA * npA + yB * npB = yres
        
        No need for a linalg solver yet.
    '''
    def find_min_tokens(self, equation: Tuple[int, int, int, int, int, int]) -> int:
        xA, yA, xB, yB, xres, yres = equation
        if 100*xA + 100*xB < xres or 100*yA + 100*yB < yres:
            return 0
        
        min_tokens = float('inf')
        for npB in range(100, -1, -1):
            target_x = xres - xB * npB
            target_y = yres - yB * npB
            
            if target_x % xA == 0 and target_y % yA == 0 and target_x // xA == target_y // yA:
                min_tokens = min(min_tokens, 3*target_x // xA + npB)
        
        if min_tokens > 400:
            return 0
        return min_tokens
    
    def calculate_min_tokens_needed(self) -> int:
        tokens = 0
        for equation in self.equations:
            tokens += self.find_min_tokens(equation)
        return tokens

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_min_tokens_needed())
