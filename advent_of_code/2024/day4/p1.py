from typing import List

class Solution():
    def __init__(self, input_file: str):
        self.DELTAS = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
        self.XMAS = ['M', 'A', 'S']
        
        self.matrix = self.read_matrix(input_file)
        
    
    def read_matrix(self, input_file: str) -> List[str]:
        matrix = []
        with open(input_file) as f:
            for line in f:
                if line[-1] == '\n':
                    matrix.append(line[:-1])
                else:
                    matrix.append(line)
        return matrix

    def calc_n_xmas(self):
        M, N = len(self.matrix), len(self.matrix[0])
        n_xmas = 0
        for ii in range(M):
            for jj in range(N):
                if self.matrix[ii][jj] == 'X':
                    for dx, dy in self.DELTAS:
                        nx, ny = ii, jj
                        n_xmas += 1
                        for idx in range(len(self.XMAS)):
                            nx += dx
                            ny += dy
                            if 0 <= nx < M and 0 <= ny < N and self.matrix[nx][ny] == self.XMAS[idx]:
                                continue
                            else:
                                n_xmas -= 1
                                break

        return n_xmas



if __name__ == '__main__':
    sol = Solution("input1")
    print(sol.calc_n_xmas())