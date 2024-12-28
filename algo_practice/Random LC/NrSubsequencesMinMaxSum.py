from typing import List
from bisect import *

import SimpleProfiler

class Solution:
    @SimpleProfiler.profile
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        jj, ii = 0, N-1
        bin_string = ["0"]*N

        while jj <= ii:
            if nums[ii] + nums[jj] > target:
                ii -= 1
            else:
                bin_string[N-1-ii+jj] = "1"
                jj += 1
        
        return int("".join(bin_string), 2) % (10**9+7)

# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         num_subseq = 0
#         MODN = 10**9 + 7
#         N = len(nums)

#         nums.sort()

#         jj, ii = 0, N-1
#         while jj < ii:
#             if nums[ii] + nums[jj] > target:
#                 ii -= 1
#             else:
#                 num_subseq += pow(2, ii-jj, MODN)
#                 jj += 1
        
#         if 2*nums[ii] <= target:
#             num_subseq += 1
        
#         num_subseq = num_subseq % MODN
        
#         return num_subseq

if __name__ == "__main__":
    with open('input.txt') as f:
        line = f.readline()
        nums = [int(x) for x in line.split(",")]
    
    target = 800708

    sol = Solution()

    print(sol.numSubseq(nums, target))
    SimpleProfiler.print_stats()
    
