MODN = 10**9 + 7


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        last_idx = dict()
        dp = [1]

        for idx, letter in enumerate(s):
            dp.append(dp[-1] * 2)
            if letter in last_idx:
                dp[-1] -= dp[last_idx[letter]]
            last_idx[letter] = idx

        return (dp[-1] - 1) % MODN


sol = Solution()
print(sol.distinctSubseqII("abc"))
print(sol.distinctSubseqII("aba"))
print(sol.distinctSubseqII("aaa"))
