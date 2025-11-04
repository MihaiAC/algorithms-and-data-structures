from typing import List
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        N = len(nums)
        counter = defaultdict(int)

        for num in nums[:(k-1)]:
            counter[num] += 1
        
        for ii in range(k-1, N):
            counter[nums[ii]] += 1
            
            freqs = sorted(counter.items(), key=lambda item: (-item[1], -item[0]))
            ans.append(sum(key * value for key, value in freqs[:x]))

            left_num = nums[ii-k+1]
            counter[left_num] -= 1
            if counter[left_num] == 0:
                del counter[left_num]
        
        return ans
