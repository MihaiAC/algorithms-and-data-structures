from typing import List, Dict, Tuple

class Solution:

    @staticmethod
    def computeAllDifferences(nums:List[int]) -> Dict[int, List[Tuple[int, int]]]:
        N = len(nums)

        diffs = dict()
        for ii in range(N-1):
            for jj in range(ii+1, N):
                diff = nums[jj]-nums[ii]
                if diff in diffs:
                    diffs[diff].append((ii, jj))
                else:
                    diffs[diff] = [(ii, jj)]
        
        return diffs


    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N in [0, 1, 2]:
            return 0

        # diffs[X] = all pairs of indices (i, j) such that i<j and nums[j]-nums[i]=X
        diffs = Solution.computeAllDifferences(nums)
        
        nr_slices = 0
        for diff in diffs.keys():
            chains = dict()
            pairs = dict()

            for (idx1, idx2) in diffs[diff]:
                pairs_idx1 = 0
                if idx1 in pairs:
                    pairs_idx1 = pairs[idx1]
                
                chains_idx1 = 0
                if idx1 in chains:
                    chains_idx1 = chains[idx1]
                
                if idx2 in pairs:
                    pairs[idx2] += 1
                else:
                    pairs[idx2] = 1
                
                if idx2 in chains:
                    chains[idx2] += pairs_idx1 + chains_idx1
                else:
                    chains[idx2] = pairs_idx1 + chains_idx1
                
                nr_slices += pairs_idx1 + chains_idx1
        
        return nr_slices
                            

if __name__ == '__main__':
    sol = Solution()
    nums = [7,7,7,7,7]
    print(sol.numberOfArithmeticSlices(nums))