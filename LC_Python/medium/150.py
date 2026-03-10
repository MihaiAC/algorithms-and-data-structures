from typing import List

from collections import deque
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {'+': lambda x,y: x+y, '-': lambda x,y: x-y, '*': lambda x,y: x*y, '/': lambda x,y: trunc(x/y)}

        for token in tokens:
            try:
                val = int(token)
                stack.append(val)
            except ValueError:
                op = operators[token]
                b = stack.pop()
                a = stack.pop()
                stack.append(op(a, b))
        
        return stack.pop()

if __name__ == '__main__':
    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(tokens))
