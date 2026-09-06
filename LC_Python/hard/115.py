class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        if M < N:
            return 0

        # dp[ii][jj] = nr of times t[jj:] appears as subseq
        # in s[ii:]
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for ii in range(M + 1):
            dp[ii][N] = 1

        for ii in range(M - 1, -1, -1):
            for jj in range(N - 1, -1, -1):
                if s[ii] == t[jj]:
                    dp[ii][jj] = dp[ii + 1][jj + 1] + dp[ii + 1][jj]
                else:
                    dp[ii][jj] = dp[ii + 1][jj]

        return dp[0][0]


sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))
print(sol.numDistinct("babgbag", "bag"))
