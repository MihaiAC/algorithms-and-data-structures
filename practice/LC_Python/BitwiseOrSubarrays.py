from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        curr_ors = {0}
        
        for num in arr:
            curr_ors = {num | prev_or for prev_or in curr_ors} | {num}
            # This is faster than ans.union(curr_ors) because union apparently creates a new set
            # while | modifies it in place (corresponds to __ior__)
            ans |= curr_ors
        
        return len(ans)

if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,4]
    print(sol.subarrayBitwiseORs(arr))
