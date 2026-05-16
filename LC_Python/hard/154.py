from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()

        N = len(nums)
        if(N == 1):
            return nums[0]
        elif(N == 2):
            return(min(nums[0], nums[1]))
        
        # Check trivial case.
        if(nums[0] <= nums[N-1]):
            return nums[0]
        
        left = 0
        right = N-1
        while(True):
            middle = (left + right) // 2
            if(nums[middle] < nums[middle-1]):
                return nums[middle]
            if(middle != N-1 and nums[middle] > nums[middle+1]):
                return nums[middle+1]
            if(nums[middle] <= nums[right]):
                right = middle
            else:
                left = middle                    

sol = Solution()
print(sol.findMin([2, 2, 2, 0, 1]))
print(sol.findMin([3, 1, 3]))