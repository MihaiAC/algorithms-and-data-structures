from typing import List

class Solution:
    @staticmethod
    def searchNextPair(pairs:List[List[int]], curr_pair_idx:int) -> int:
        N = len(pairs)

        right_elem = pairs[curr_pair_idx][1]

        left = curr_pair_idx+1
        right = N-1

        if right_elem >= pairs[-1][0]:
            return N
        while left < right:
            median = (left+right)//2
            if right_elem < pairs[median][0]:
                if right_elem >= pairs[median-1][0]:
                    return median
                right = median-1
            else:
                left = median+1
        
        if left == N-1 and right_elem < pairs[N-1][0]:
            return N-1
        
        if left == right:
            return left
        
        

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])

        N = len(pairs)

        maximumsFrom = dict()

        for ii in range(N-1, -1, -1):
            if ii == N-1:
                maximumsFrom[ii] = 1
            else:
                if pairs[ii][1] < pairs[ii+1][0]:
                    maximumsFrom[ii] = maximumsFrom[ii+1] + 1
                else:
                    jj = Solution.searchNextPair(pairs, ii)
                    if jj == N:
                        maximumsFrom[ii] = max(1, maximumsFrom[ii+1])
                    else:
                        maximumsFrom[ii] = max(maximumsFrom[jj]+1, maximumsFrom[ii+1])


        return maximumsFrom[0]

if __name__ == '__main__':
    sol = Solution()
    pairs = [[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]]

    print(sol.findLongestChain(pairs))