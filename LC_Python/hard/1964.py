from typing import List
import SimpleProfiler
import unittest
from bisect import bisect_right

class Solution:
    @SimpleProfiler.profile
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        N = len(obstacles)
        smallest_last_elem = [0]
        max_so_far = 1

        for idx in range(N):
            kk = bisect_right(smallest_last_elem, obstacles[idx], 0, max_so_far)
            
            if kk == max_so_far:
                max_so_far += 1
                smallest_last_elem.append(obstacles[idx])
            else:
                smallest_last_elem[kk] = min(obstacles[idx], smallest_last_elem[kk])
            
            obstacles[idx] = kk
        
        return obstacles

    
class SolutionTest(unittest.TestCase):
    def test_solution_1(self):
        obstacles = [1,2,3,2]
        result = [1,2,3,3]
        sol = Solution()

        self.assertEqual(sol.longestObstacleCourseAtEachPosition(obstacles), result)
    
    def test_solution_2(self):
        obstacles = [2,2,1]
        result = [1,2,1]
        sol = Solution()
        
        self.assertEqual(sol.longestObstacleCourseAtEachPosition(obstacles), result)
    
    def test_solution_3(self):
        obstacles = [3,1,5,6,4,2]
        result = [1,1,2,3,2,2]
        sol = Solution()
        
        self.assertEqual(sol.longestObstacleCourseAtEachPosition(obstacles), result)

if __name__=='__main__':
    # unittest.main()

    obstacles = []
    sol = Solution()
    sol.longestObstacleCourseAtEachPosition(obstacles)
    SimpleProfiler.print_stats()
    