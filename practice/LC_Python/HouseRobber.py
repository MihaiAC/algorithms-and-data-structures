from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])
        
        arr = [nums[0], nums[1], max(nums[2]+nums[0], nums[1])]

        for ii in range(3, len(nums)):
            curr = max(arr[0], arr[1]) + nums[ii]
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = curr
        
        return max(arr[1], arr[2])