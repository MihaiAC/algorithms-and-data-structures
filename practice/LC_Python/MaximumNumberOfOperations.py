class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        curr_ones = 1 if s[0] == '1' else 0

        for idx in range(1, len(s)):
            if s[idx] == '1':
                curr_ones += 1
            elif s[idx-1] == '1':
                ans += curr_ones
        
        return ans