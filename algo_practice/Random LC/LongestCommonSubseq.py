import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)

        grid = np.full((N1+1, N2+1), 0, dtype=np.int8)

        for ii in range(1, N1+1):
            for jj in range(1, N2+1):
                if text1[ii-1] == text2[jj-1]:
                    grid[ii][jj] = grid[ii-1][jj-1] + 1
                else:
                    grid[ii][jj] = max(grid[ii-1][jj], grid[ii][jj-1])

        return grid[N1][N2]


if __name__ == '__main__':
    sol = Solution()
    text1 = 'abcd'
    text2 = 'abc'

    print(sol.longestCommonSubsequence(text1, text2))