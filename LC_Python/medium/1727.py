from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        ans = 0
        prev_row = [0] * N

        for ii in range(M):
            curr_row = matrix[ii][:]

            for jj in range(N):
                if curr_row[jj] == 1:
                    curr_row[jj] += prev_row[jj]

            sorted_row = sorted(curr_row, reverse=True)
            for jj in range(N):
                if sorted_row[jj] == 0:
                    break
                ans = max(ans, sorted_row[jj] * (jj + 1))

            prev_row = curr_row

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert sol.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4
    assert sol.largestSubmatrix([[1, 0, 1, 0, 1]]) == 3
    assert sol.largestSubmatrix([[1, 1, 0], [1, 0, 1]]) == 2
