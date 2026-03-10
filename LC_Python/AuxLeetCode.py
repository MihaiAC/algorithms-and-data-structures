from sys import argv

from typing import Tuple, List
from enum import Enum

class Operation(Enum):
    ADD = 1
    SUB = 2
    NOOP = 3

class Solution:
    digits = "0123456789"

    # observations: ignore spaces, decide when - is unary or binary.
    @staticmethod
    def readNumber(s:str, idx:int) -> Tuple[int, int]:
        number = 0
        while idx < len(s) and s[idx] in Solution.digits:
            number = number*10 + int(s[idx])
            idx += 1
        return number, idx
    
    @staticmethod
    def skipSpaces(s:str, idx:int) -> int:
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        return idx
    
    @staticmethod
    def performOp(nr1:int, nr2:int, op:Operation):
        if op == Operation.ADD:
            return nr1 + nr2
        elif op == Operation.SUB:
            return nr1 - nr2
        else:
            print("Tried to perform NOOP.")
            exit()

    @staticmethod
    # Returns what the paranthesis evaluates to and the index of the character after ')'.
    def evaluateParanthesis(s:str, idx: int) -> Tuple[int, int]:
        current_sum = 0
        previous_operation = Operation.NOOP

        idx = Solution.skipSpaces(s, idx)

        if s[idx] == '-':
            if s[idx+1] == ' ':
                idx = Solution.skipSpaces(s, idx+1)
                idx -= 1

            if s[idx+1] in Solution.digits:
                number, new_idx = Solution.readNumber(s, idx+1)
                current_sum = -number
                idx = new_idx
            elif s[idx+1] == '(':
                eval_par, new_idx = Solution.evaluateParanthesis(s, idx+2)
                current_sum = -eval_par
                idx = new_idx
            else:
                print(idx)
                print("Possible logical error in evaluateParanthesis.")
                exit()
        
        while idx < len(s) and s[idx] != ')':
            if s[idx] == ' ':
                idx += 1
            elif s[idx] == '+':
                previous_operation = Operation.ADD
                idx += 1
            elif s[idx] == '-':
                previous_operation = Operation.SUB
                idx += 1
            elif s[idx] in Solution.digits:
                number, new_idx = Solution.readNumber(s, idx)
                if previous_operation == Operation.NOOP:
                    current_sum = number
                else:
                    current_sum = Solution.performOp(current_sum, number, previous_operation)
                previous_operation = Operation.NOOP
                idx = new_idx
            elif s[idx] == '(':
                number, new_idx = Solution.evaluateParanthesis(s, idx+1)
                if previous_operation == Operation.NOOP:
                    current_sum = number
                else:
                    current_sum = Solution.performOp(current_sum, number, previous_operation)
                    previous_operation = Operation.NOOP
                idx = new_idx
            else:
                print("Unidentified character encountered in evaluateParanthesis.")
                exit()
        
        return current_sum, idx+1
            

    def calculate(self, s: str) -> int:
        result, _ = Solution.evaluateParanthesis(s, 0)
        return result


if __name__ == '__main__':
    s = "1-(     -2)"
    sol = Solution()
    print(sol.calculate(s))

