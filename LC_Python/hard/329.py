from typing import List, Tuple

class Solution:
    @staticmethod
    def getValidNeighbors(px: int, py: int, M: int, N: int) -> List[Tuple[int, int]]:
        valid_neighbors = []
        for nx, ny in [(px+1, py), (px-1, py), (px, py+1), (px, py-1)]:
            if nx >= M or ny >= N or nx < 0 or ny < 0:
                continue
            else:
                valid_neighbors.append((nx, ny))
        
        return valid_neighbors

    def longestIncreasingPathFrom(self, matrix: List[List[int]], px: int, py: int) -> int:
        if (px, py) in self.longest_path_from:
            return self.longest_path_from[(px, py)]
        
        longest_neighbor_path = 0
        for (nx, ny) in Solution.getValidNeighbors(px, py, len(matrix), len(matrix[0])):
            if matrix[nx][ny] > matrix[px][py]:
                longest_path = 0
                if (nx, ny) in self.longest_path_from:
                    longest_path = self.longest_path_from[(nx, ny)]
                else:
                    longest_path = self.longestIncreasingPathFrom(matrix, nx, ny)
                if longest_path > longest_neighbor_path:
                    longest_neighbor_path = longest_path

        self.longest_path_from[(px, py)] = 1 + longest_neighbor_path

        return 1 + longest_neighbor_path

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.longest_path_from = dict()

        global_max_path = 0
        for ii in range(len(matrix)):
            for jj in range(len(matrix[0])):
                local_max_path = self.longestIncreasingPathFrom(matrix, ii, jj)
                if local_max_path > global_max_path:
                    global_max_path = local_max_path
        
        return global_max_path

if __name__ == '__main__':
    sol = Solution()
    matrix = [
        [1,8,7],
        [2,7,6],
        [3,4,5]]
    print(sol.longestIncreasingPath(matrix))