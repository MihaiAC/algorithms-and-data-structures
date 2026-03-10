from collections import deque

class Solution:
    def __init__(self, input_file: str):
        self.matrix = []
        with open(input_file) as f:
            for line in f:
                if line != '\n':
                    self.matrix.append(line[:-1])
    
    def calculate_price(self) -> int:
        total_price = 0
        M, N = len(self.matrix), len(self.matrix[0])
        visited = [[0 for _ in range(N)] for _ in range(M)]
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for ii in range(M):
            for jj in range(N):
                if visited[ii][jj] == 0:
                    visited[ii][jj] = 1
                    current_letter = self.matrix[ii][jj]
                    current_perimeter = 0
                    current_area = 0
                    queue = deque()
                    queue.appendleft((ii, jj))
                    while len(queue) > 0:
                        cx, cy = queue.pop()
                        current_area += 1
                        for dx, dy in deltas:
                            if 0 <= cx+dx < M and 0 <= cy+dy < N:
                                if self.matrix[cx+dx][cy+dy] != current_letter:
                                    current_perimeter += 1
                                elif visited[cx+dx][cy+dy] == 0:
                                    queue.appendleft((cx+dx, cy+dy))
                                    visited[cx+dx][cy+dy] = 1
                            else:
                                current_perimeter += 1
                    total_price += current_area * current_perimeter
        
        return total_price


if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_price())