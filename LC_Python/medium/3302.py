from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        M, N = len(word1), len(word2)
        # dp[idx] = x => starting from idx in word1, the max suffix of word2 that
        # we can match has length x
        dp = [0] * (M + 1)

        for idx in range(M - 1, -1, -1):
            if dp[idx + 1] < N and word1[idx] == word2[N - dp[idx + 1] - 1]:
                dp[idx] = dp[idx + 1] + 1
            else:
                dp[idx] = dp[idx + 1]

        # Build ans.
        ans = []
        idx1, idx2 = 0, 0
        used_change = False

        while idx1 < M and idx2 < N:
            if word1[idx1] == word2[idx2]:
                ans.append(idx1)
                idx2 += 1
            elif not used_change and dp[idx1 + 1] >= N - idx2 - 1:
                # Using change here => we can still construct the remaining word2 +
                # ans is lexicographically smallest.
                ans.append(idx1)
                used_change = True
                idx2 += 1

            idx1 += 1

        return ans if idx2 == N else []


sol = Solution()
print(sol.validSequence("vbcca", "abc"))
print(sol.validSequence("bacdc", "abc"))
print(sol.validSequence("aaaaaa", "aaabc"))
print(sol.validSequence("abc", "ab"))
