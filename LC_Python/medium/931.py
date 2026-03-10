from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        if N == 1:
            return matrix[0][0]
        
        min_prev = []
        for elem in matrix[N-1]:
            min_prev.append(elem)
        
        min_curr = [0] * N

        for ii in range(N-2, -1, -1):

            min_curr[0] = min(min_prev[0], min_prev[1]) + matrix[ii][0]
            for jj in range(1, N-1):
                min_curr[jj] = min(min_prev[jj-1], min_prev[jj], min_prev[jj+1]) + matrix[ii][jj]
            min_curr[N-1] = min(min_prev[N-2], min_prev[N-1]) + matrix[ii][N-1]

            aux = min_prev
            min_prev = min_curr
            min_curr = aux
        
        return min(min_prev)

if __name__ == '__main__':
    sol = Solution()
    matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]

    print(sol.minFallingPathSum(matrix))