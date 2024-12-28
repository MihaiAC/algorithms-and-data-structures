from typing import List

import numpy as np

class Solution:
    @staticmethod
    def searchPreviousNonOverlappingWindow(startTime: int, endTime: List[int], sortedIndices: List[int], start_index: int) -> int:
        true_startIndex = sortedIndices[start_index]
        if endTime[true_startIndex] <= startTime:
            return start_index
        
        if endTime[sortedIndices[0]] > startTime:
            return -1
        
        left = 0
        right = start_index

        while left <= right:
            middle = (left+right)//2
            if endTime[sortedIndices[middle]] <= startTime:
                if startTime < endTime[sortedIndices[middle+1]]:
                    return middle
                else:
                    left = middle+1
            else:
                right = middle-1
        
        return -1



    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sortedIndices = np.argsort(endTime)
        max_profit = []

        for ii in range(len(sortedIndices)):
            if ii == 0:
                max_profit.append(profit[sortedIndices[ii]])
                continue
            
            # Calculate profit if we include current element (could reach start).
            # We need to find true index jj so that true_jj < true_ii and endtime[true_jj] <= startTime[true_ii].
            jj = Solution.searchPreviousNonOverlappingWindow(startTime[sortedIndices[ii]], endTime, sortedIndices, ii-1)
            found = jj >= 0
            
            max_profit_with_ii = 0
            if found:
                max_profit_with_ii = profit[sortedIndices[ii]] + max_profit[jj]
            else:
                max_profit_with_ii = profit[sortedIndices[ii]]

            max_profit_without_ii = max_profit[ii-1]
            max_profit.append(max(max_profit_with_ii, max_profit_without_ii))
        
        return max_profit[-1]

if __name__ == '__main__':
    sol = Solution()
    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    print(sol.jobScheduling(startTime, endTime, profit))