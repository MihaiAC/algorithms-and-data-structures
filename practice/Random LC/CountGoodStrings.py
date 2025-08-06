import SimpleProfiler
import unittest
from collections import defaultdict

class Solution:
    @SimpleProfiler.profile
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        counts = [0] * (high + 1)
        counts[0] = 1
        mod = 10**9 + 7

        for ii in range(1, high+1):
            counts[ii] = (counts[ii-zero] + counts[ii-one]) % mod
        
        return sum([counts[ii] for ii in range(low, high+1)]) % mod

    
class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_solution_1(self):
        low = 3
        high = 3
        zero = 1
        one = 1
        result = 8

        self.assertEqual(self.sol.countGoodStrings(low, high, zero, one), result)
    
    def test_solution_2(self):
        low = 2
        high = 3
        zero = 1
        one = 2
        result = 5
        
        self.assertEqual(self.sol.countGoodStrings(low, high, zero, one), result)

if __name__=='__main__':
    unittest.main()

    # sol = Solution()
    # sol.countGoodStrings(45360, 45360, 10, 2)
    # SimpleProfiler.print_stats()
    