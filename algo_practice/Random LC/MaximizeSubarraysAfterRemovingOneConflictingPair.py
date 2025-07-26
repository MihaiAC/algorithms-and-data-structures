from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrays(self, N: int, conflictingPairs: List[List[int]]) -> int:
        conflictsStartingAt = defaultdict(list)
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            conflictsStartingAt[a].append(b)
        
        ans = 0
        gainByPair = defaultdict(int)
        firstBlockerB = N+1
        firstBlockerA = N+1
        secondBlockerB = N+1

        for idx in range(N, 0, -1):
            # Add all b values starting at this idx.
            for b in conflictsStartingAt[idx]:
                if b < firstBlockerB:
                    secondBlockerB = firstBlockerB
                    firstBlockerB = b
                    firstBlockerA = idx
                elif b < secondBlockerB:
                    secondBlockerB = b
            
            # Subarrays starting at idx can normally go up to firstBlockerB-1.
            ans += firstBlockerB-idx

            # Potential gain from deleting the conflict that caused firstBlockerB.
            gain = secondBlockerB - firstBlockerB
            if gain > 0:
                gainByPair[(firstBlockerA, firstBlockerB)] += gain
        
        return ans + max(gainByPair.values(), default=0)
    
if __name__ == '__main__':
    sol = Solution()
    N = 4
    pairs = [[2,3],[1,4]]
    print(sol.maxSubarrays(N, pairs))