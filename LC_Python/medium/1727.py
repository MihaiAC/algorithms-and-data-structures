from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        nrows, ncols, ans = len(matrix), len(matrix[0]), 0

        for ncol in range(ncols):
            for nrow in range(1, nrows):
                matrix[nrow][ncol] *= 1 + matrix[nrow - 1][ncol]

        for nrow in range(nrows):
            matrix[nrow].sort(reverse=True)
            for ncol in range(ncols):
                if matrix[nrow][ncol] == 0:
                    break
                ans = max(ans, matrix[nrow][ncol] * (ncol + 1))

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert sol.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4
    assert sol.largestSubmatrix([[1, 0, 1, 0, 1]]) == 3
    assert sol.largestSubmatrix([[1, 1, 0], [1, 0, 1]]) == 2
