from collections import deque

class Solution:
    def __init__(self, input_file):
        self.matrix = []
        with open(input_file) as f:
            for line in f:
                if line == '\n':
                    break
                self.matrix.append([int(line[idx]) for idx in range(len(line)-1)])
    
    def calculate_score_sum(self):
        score_sum = 0
        deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        M, N = len(self.matrix), len(self.matrix[0])

        for ii in range(M):
            for jj in range(N):
                if self.matrix[ii][jj] == 0:
                    reached = set()
                    queue = deque([(ii, jj)])
                    while len(queue) > 0:
                        cx, cy = queue.pop()
                        if self.matrix[cx][cy] == 9:
                            reached.add((cx, cy))
                        else:
                            for dx, dy in deltas:
                                if 0 <= cx+dx < M and 0 <= cy+dy < N and self.matrix[cx+dx][cy+dy] == self.matrix[cx][cy]+1:
                                    queue.appendleft((cx+dx, cy+dy))
                    score_sum += len(reached)
        
        return score_sum

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_score_sum())
                        
