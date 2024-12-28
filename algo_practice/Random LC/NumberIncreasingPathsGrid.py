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

    def countPathsFrom(self, matrix: List[List[int]], px: int, py: int) -> int:
        if (px, py) in self.count_paths_from:
            return self.count_paths_from[(px, py)]
        
        count_paths = 0
        for (nx, ny) in Solution.getValidNeighbors(px, py, len(matrix), len(matrix[0])):
            if matrix[nx][ny] > matrix[px][py]:
                count_paths += self.countPathsFrom(matrix, nx, ny)
                count_paths = count_paths % self.modulo

        count_paths += 1
        
        self.count_paths_from[(px, py)] = count_paths
        return count_paths

    def countPaths(self, matrix: List[List[int]]) -> int:
        self.count_paths_from = dict()
        self.modulo = 10**9+7

        total_paths = 0
        for ii in range(len(matrix)):
            for jj in range(len(matrix[0])):
                total_paths += self.countPathsFrom(matrix, ii, jj)
                total_paths = total_paths % self.modulo
        
        return total_paths

if __name__ == '__main__':
    sol = Solution()
    grid = [[1],[2]]
    print(sol.countPaths(grid))
    print(sol.count_paths_from)