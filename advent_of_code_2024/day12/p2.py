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
        orthogonal = {
            (0, 1): [(-1, 0), (1, 0)],
            (0, -1): [(-1, 0), (1, 0)],
            (1, 0): [(0, 1), (0, -1)],
            (-1, 0): [(0, 1), (0, -1)]
        }
        within_bounds = lambda x, y: 0 <= x < M and 0 <= y < N

        for ii in range(M):
            for jj in range(N):
                if visited[ii][jj] == 0:
                    current_letter = self.matrix[ii][jj]
                    current_sides = 0
                    current_area = 0
                    queue = deque()
                    queue.appendleft((ii, jj))
                    while len(queue) > 0:
                        cx, cy = queue.pop()
                        if visited[cx][cy]:
                            continue
                        else:
                            visited[cx][cy] += 1
                        current_area += 1
                        for dx, dy in deltas:
                            if within_bounds(cx+dx, cy+dy):
                                if self.matrix[cx+dx][cy+dy] != current_letter:
                                    counted_side = False
                                    for ox, oy in orthogonal[(dx, dy)]:
                                        if within_bounds(cx+ox, cy+oy):
                                            if visited[cx+ox][cy+oy] and self.matrix[cx+ox][cy+oy] == current_letter and self.matrix[cx+ox+dx][cy+oy+dy] != current_letter:
                                                counted_side = True
                                                break
                                    if not counted_side:
                                        current_sides += 1
                                elif visited[cx+dx][cy+dy] == 0:
                                    queue.appendleft((cx+dx, cy+dy))
                            else:
                                counted_side = False
                                for ox, oy in orthogonal[(dx, dy)]:
                                    if within_bounds(cx+ox, cy+oy):
                                        if visited[cx+ox][cy+oy] and self.matrix[cx+ox][cy+oy] == current_letter and not within_bounds(cx+ox+dx, cy+oy+dy):
                                            counted_side = True
                                            break
                                if not counted_side:
                                    current_sides += 1
                    total_price += current_area * current_sides        
        return total_price


if __name__ == '__main__':
    sol = Solution('test')
    print(sol.calculate_price())