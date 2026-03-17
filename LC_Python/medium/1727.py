from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        ans = 0
        prev_heights = []

        for ii in range(M):
            heights = []
            seen = [False] * N

            # Increment heights, maintains order assuming prev_heights were sorted
            for height, jj in prev_heights:
                if matrix[ii][jj] == 1:
                    heights.append((height + 1, jj))
                    seen[jj] = True

            # Add new heights.
            for jj in range(N):
                if matrix[ii][jj] == 1 and not seen[jj]:
                    heights.append((1, jj))

            # Update ans
            for jj in range(len(heights)):
                ans = max(ans, heights[jj][0] * (jj + 1))

            prev_heights = heights

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert sol.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4
    assert sol.largestSubmatrix([[1, 0, 1, 0, 1]]) == 3
    assert sol.largestSubmatrix([[1, 1, 0], [1, 0, 1]]) == 2
