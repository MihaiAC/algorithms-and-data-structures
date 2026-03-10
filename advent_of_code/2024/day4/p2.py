from typing import List

class Solution():
    def __init__(self, input_file: str):
        self.DELTAS = [[(-1,-1,'M'),(1,1,'S'),(1,-1,'M'),(-1,1,'S')],
                       [(-1,-1,'S'),(1,1,'M'),(1,-1,'M'),(-1,1,'S')],
                       [(-1,-1,'S'),(1,1,'M'),(1,-1,'S'),(-1,1,'M')],
                       [(-1,-1,'M'),(1,1,'S'),(1,-1,'S'),(-1,1,'M')]
                       ]
        
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
                if self.matrix[ii][jj] == 'A':
                    for delta in self.DELTAS:
                        n_xmas += 1
                        for dx, dy, letter in delta:
                            nx, ny = ii+dx, jj+dy
                            if 0 <= nx < M and 0 <= ny < N and self.matrix[nx][ny] == letter:
                                continue
                            else:
                                n_xmas -= 1
                                break

        return n_xmas



if __name__ == '__main__':
    sol = Solution("input1")
    print(sol.calc_n_xmas())