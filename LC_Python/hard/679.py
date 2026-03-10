from itertools import product, permutations
from typing import List
from math import isclose

SIGNS = ['+', '-', '*', '/']

# open_parens[0], closed_parens[0] define the indices we should add parantheses to
open_parens = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)]
closed_parens = [(1, 2), (2, 2), (1, 3), (2, 3), (3, 3)]

def insert_signs(expr, signs):
    out = []
    op_index = 0

    for idx, token in enumerate(expr):
        out.append(token)

        if op_index < len(signs):
            if (token != '(') and (idx + 1 == len(expr) or expr[idx + 1] != ")"):
                out.append(signs[op_index])
                op_index += 1

    return out

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        for numbers in permutations(cards):
            expr = [str(num) for num in numbers]
            for idx in range(len(open_parens)):
                parens = [(closed_parens[idx][0], ')'), (closed_parens[idx][1], ')'), (open_parens[idx][0], '('), (open_parens[idx][1], '(')]
                parens.sort(key=lambda x: x[0], reverse=True)
                
                expr_copy = expr[:]
                for paren_idx, paren in parens:
                    if paren == '(':
                        expr_copy[paren_idx] = '(' + expr_copy[paren_idx]
                    else:
                        expr_copy[paren_idx] += ')'
                
                for signs in product(SIGNS, repeat=len(SIGNS)-1):
                    final_expr = insert_signs(expr_copy, signs)

                    try:
                        val = eval("".join(final_expr))
                        if isclose(val, 24):
                            return True
                    except ZeroDivisionError as e:
                        continue
        
        return False
        