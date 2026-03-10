class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0
        
        nz = [N]*N
        last_pos = N
        for ii in range(N-1, -1, -1):
            nz[ii] = last_pos
            if s[ii] == '0':
                last_pos = ii

        for ii in range(N-1, -1, -1):
            zeros = 1 if s[ii] == '0' else 0
            next_idx = ii
            curr_idx = ii
            
            while curr_idx < N and zeros**2 <= N:
                next_idx = nz[curr_idx]
                ones = next_idx - zeros - ii

                if zeros**2 <= ones:
                    ans += min(next_idx-curr_idx, ones - zeros**2 + 1)
                
                curr_idx = next_idx
                zeros += 1

        return ans