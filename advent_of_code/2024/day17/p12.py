import re
from math import floor
from typing import Set

class Solution:
    def __init__(self, input_file: str):
        pattern = re.compile('[0-9]+')
        nums = pattern.findall(open(input_file).read())
        
        self.A = int(nums[0])
        self.B = int(nums[1])
        self.C = int(nums[2])

        self.instructions = [int(x) for x in nums[3:]]
    
    def combo(self, idx: int) -> int:
        instr = self.instructions[idx]
        if instr <= 3:
            return instr
        elif instr == 4:
            return self.A
        elif instr == 5:
            return self.B
        elif instr == 6:
            return self.C
        raise ValueError(f"Error for instr={instr}")

    def calculate_output(self, A:int=None) -> str:
        if A != None:
            self.A = A
        
        idx = 0
        out = []
        adv = lambda k: floor(self.A/2**self.combo(k+1))

        while idx < len(self.instructions):
            instr = self.instructions[idx]
            if instr == 3:
                if self.A == 0:
                    idx += 2
                else:
                    idx = self.instructions[idx+1]
            else:
                if instr == 0:
                    self.A = adv(idx)
                elif instr == 1:
                    self.B = self.B ^ self.instructions[idx+1]
                elif instr == 2:
                    self.B = self.combo(idx+1) % 8
                elif instr == 4:
                    self.B = self.B ^ self.C
                elif instr == 5:
                    out.append(str(self.combo(idx+1)%8))
                elif instr == 6:
                    self.B = adv(idx)
                elif instr == 7:
                    self.C = adv(idx)
                idx += 2
        
        return ",".join(out)
    
    def reverse(self) -> Set[int]:
        # Input-dependent expression, constructed by hand.
        # Could have done something smarter, since only the last 3 bits of X matter, 
        # but it worked so that's good enough.
        bxcout = lambda X: ((X%8)^floor(X/2**(7-X%8)))%8
        curr_poss = set([7])
        for idx in range(len(self.instructions)-2, -1, -1):
            # X has to be greater than 8.
            next_poss = set()
            for poss in curr_poss:
                min_range = 8*poss
                max_range = 8*(poss+1)
                for X in range(min_range, max_range):
                    if X > 8 and self.instructions[idx] == bxcout(X):
                        next_poss.add(X)
            curr_poss = next_poss
        return min(curr_poss)
        


if __name__ == '__main__':
    sol = Solution('input')
    # print(sol.calculate_output(265601188299675))
    print(sol.reverse())