import SimpleProfiler
import unittest
from typing import List
from collections import defaultdict, deque

class Solution:
    @SimpleProfiler.profile
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = dict()

        # Union find to find out if two variables are part of the same connected component.
        def find_parent(var: str) -> str:
            if var not in parent:
                parent[var] = var
                return var
            elif var == parent[var]:
                return var
            else:
                parent[var] = find_parent(parent[var])
                return parent[var]
        
        def union(var1: str, var2: str):
            par1 = find_parent(var1)
            par2 = find_parent(var2)

            if par1 != par2:
                parent[par1] = par2
        
        link = defaultdict(list)
        multiplier = dict()
        for ii in range(len(equations)):
            numerator = equations[ii][0]
            denominator = equations[ii][1]
            value = values[ii]

            union(numerator, denominator)

            link[numerator].append(denominator)
            link[denominator].append(numerator)

            multiplier[(numerator, denominator)] = value
            multiplier[(denominator, numerator)] = 1/value
        
        result = []
        for query in queries:
            numerator, denominator = query

            if numerator not in parent or denominator not in parent:
                result.append(-1)
                continue

            par_numerator = find_parent(numerator)
            par_denominator = find_parent(denominator)

            if par_numerator != par_denominator:
                result.append(-1)
                continue
            
            queue = deque()
            queue.appendleft((numerator, 1))

            visited = set()
            visited.add(numerator)

            while True:
                var, mult = queue.pop()
                if var == denominator:
                    result.append(mult)
                    break
                for var_2 in link[var]:
                    if var_2 not in visited:
                        visited.add(var_2)
                        queue.appendleft((var_2, mult*multiplier[(var, var_2)]))
                
        return result

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_solution_1(self):
        equations = [["a","b"],["b","c"]]
        values = [2.0,3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        
        result = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
        
        self.assertEqual(self.sol.calcEquation(equations, values, queries), result)
    
    def test_solution_2(self):
        equations = [["a","b"],["b","c"],["bc","cd"]]
        values = [1.5,2.5,5.0]
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        
        result = [3.75000,0.40000,5.00000,0.20000]
        
        self.assertEqual(self.sol.calcEquation(equations, values, queries), result)
    
    def test_solution_3(self):
        equations = [["a","b"]]
        values = [0.5]
        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
        
        result = [0.50000,2.00000,-1.00000,-1.00000]
        
        self.assertEqual(self.sol.calcEquation(equations, values, queries), result)

if __name__ == '__main__':
    # unittest.main()
    
    sol = Solution()
    sol.calcEquation(equations = [["a","b"],["b","c"]],
                    values = [2.0,3.0],
                    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    
    SimpleProfiler.print_stats()
    
