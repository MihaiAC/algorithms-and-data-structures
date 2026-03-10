from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)

        ans = 0
        for ii in range(N):
            counter = defaultdict(int)
            for jj in range(ii, N):
                counter[s[jj]] += 1
                if len(set(counter.values())) == 1:
                    ans = max(ans, jj - ii + 1)

        return ans
