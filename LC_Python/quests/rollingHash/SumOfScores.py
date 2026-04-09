# z-function: https://cp-algorithms.com/string/z-function.html
class Solution:
    def sumScores(self, s: str) -> int:
        N = len(s)
        z = [0] * N
        left, right = 0, 0
        for ii in range(1, N):
            # We know that [left, right) is a prefix.
            # If left <= ii < right => we can try to retrieve a partial match.
            # z[ii-left] is this partial match.
            # But its length cannot exceed right, since we haven't parsed that yet.
            if ii < right:
                z[ii] = min(right - ii, z[ii - left])

            # Extend current match.
            while ii + z[ii] < N and s[z[ii]] == s[ii + z[ii]]:
                z[ii] += 1

            # Right must always be the rightmost character we parsed.
            if ii + z[ii] > right:
                left, right = ii, ii + z[ii]

        return N + sum(z)


sol = Solution()
print(sol.sumScores("babab"))
print(sol.sumScores("azbazbzaz"))
print(sol.sumScores("ky"))
print(sol.sumScores("optmchspszpneevqvirbonchto"))
