from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for idx in range(len(target)-1):
            if target[idx+1] > target[idx]:
                ans += target[idx+1] - target[idx]
        return ans
    
if __name__ == '__main__':
    sol = Solution()
    target = [1, 2, 3, 2, 1]
    print(sol.minNumberOperations(target))