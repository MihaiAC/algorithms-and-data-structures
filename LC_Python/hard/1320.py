LETTERS = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZ"]
DIST = [[0 for _ in range(26)] for _ in range(26)]
COORDS = dict()

for ii in range(5):
    for jj in range(6):
        # Last row
        if jj >= len(LETTERS[ii]):
            continue

        letter_idx = ord(LETTERS[ii][jj]) - ord("A")
        COORDS[letter_idx] = (ii, jj)

for l1 in range(26):
    x1, y1 = COORDS[l1]
    for l2 in range(26):
        x2, y2 = COORDS[l2]
        DIST[l1][l2] = DIST[l2][l1] = abs(x1 - x2) + abs(y1 - y2)


class Solution:
    def minimumDistance(self, word: str) -> int:
        # dp[ii][jj][kk] = minimum distance if finger 1 is on ii, finger 2 on jj and we've typed word[:k]
        N = len(word)
        prev = [[0 for _ in range(26)] for _ in range(26)]
        curr = [[0 for _ in range(26)] for _ in range(26)]

        for kk in range(N - 1, -1, -1):
            letter = ord(word[kk]) - ord("A")
            for ii in range(26):
                for jj in range(26):
                    curr[ii][jj] = min(
                        DIST[ii][letter] + prev[letter][jj],
                        DIST[jj][letter] + prev[ii][letter],
                    )
            curr, prev = prev, curr

        return min([min(row) for row in prev])


sol = Solution()
print(sol.minimumDistance("CAKE"))
print(sol.minimumDistance("HAPPY"))
