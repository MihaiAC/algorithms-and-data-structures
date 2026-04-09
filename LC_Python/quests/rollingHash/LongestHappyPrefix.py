class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)

        # lps[i] = x => s[0..(x-1)] == s[(i-x+1)..i]
        lps = [0] * N

        for ii in range(1, N):
            jj = lps[ii - 1]
            while jj > 0 and s[ii] != s[jj]:
                jj = lps[jj - 1]

            if s[ii] == s[jj]:
                jj += 1

            lps[ii] = jj

        return s[: lps[N - 1]]


sol = Solution()
print(sol.longestPrefix("level"))
print(sol.longestPrefix("ababab"))
