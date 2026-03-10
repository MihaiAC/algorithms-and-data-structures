from collections import defaultdict

class Solution:
    def __init__(self, input_file):
        self.matrix = []
        with open(input_file) as f:
            for line in f:
                if line == '\n':
                    break
                self.matrix.append([int(line[idx]) for idx in range(len(line)-1)])
    
    def calculate_score_sum(self):
        deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        M, N = len(self.matrix), len(self.matrix[0])
        npaths = [[0 for _ in range(M)] for _ in range(N)]

        num_to_coords = defaultdict(list)
        for ii in range(M):
            for jj in range(N):
                num_to_coords[self.matrix[ii][jj]].append((ii, jj))
        
        score_sum = 0
        for digit in range(9, -1, -1):
            for cx, cy in num_to_coords[digit]:
                if digit == 9:
                    npaths[cx][cy] = 1
                else:
                    for dx, dy in deltas:
                        if 0 <= cx+dx < M and 0 <= cy+dy < N and self.matrix[cx+dx][cy+dy] == digit+1:
                            npaths[cx][cy] += npaths[cx+dx][cy+dy]
                    if digit == 0:
                        score_sum += npaths[cx][cy]
        
        return score_sum


if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_score_sum())
                        
