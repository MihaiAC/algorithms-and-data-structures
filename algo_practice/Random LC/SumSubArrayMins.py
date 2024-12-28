from typing import List

from collections import deque

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = [1]*len(arr)
        right = [1]*len(arr)

        stack = deque()
        stack.append(-1)

        for ii in range(1, len(arr)):
            if arr[ii-1] > arr[ii]:
                count = 1
                idx = ii-1

                while idx >= 0 and arr[ii] < arr[idx]:
                    count += idx-stack[-1]
                    idx = stack.pop()
                
                stack.append(idx)
                left[ii] = count

            else:
                stack.append(ii-1)
        
        stack = deque()
        stack.append(len(arr))

        for ii in range(len(arr)-2, -1, -1):
            if arr[ii] <= arr[ii+1]:
                count = 1
                idx = ii+1

                while idx <= len(arr)-1 and arr[ii] <= arr[idx]:
                    count += stack[-1]-idx
                    idx = stack.pop()
                
                stack.append(idx)
                right[ii] = count
            
            else:
                stack.append(ii+1)
        
        requested_sum = 0
        for ii in range(len(arr)):
            requested_sum += arr[ii] * (left[ii] + right[ii] - 1 + (left[ii]-1)*(right[ii]-1))
        
        print(left)
        print(right) 

        return requested_sum % (10**9 + 7)


if __name__ == "__main__":
    sol = Solution()
    arr = [71,55,82,55]
    print(sol.sumSubarrayMins(arr))