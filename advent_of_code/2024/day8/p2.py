from collections import defaultdict

class Solution:
    def __init__(self, input_file: str):
        self.matrix = []
        with open(input_file) as f:
            for line in f:
                if line != '\n':
                    self.matrix.append(line[:-1])

        self.M = len(self.matrix)
        self.N = len(self.matrix[0])

    def count_locations(self) -> int:
        antennas = defaultdict(list)
        antinodes = set()
        for ii in range(self.M):
            for jj in range(self.N):
                if self.matrix[ii][jj] != '.':
                    antennas[self.matrix[ii][jj]].append((ii, jj))
                    antinodes.add((ii, jj))
        
        for symbol in antennas:
            coords = antennas[symbol]
            if len(coords) > 1:
                for idx1 in range(len(coords)-1):
                    x1, y1 = coords[idx1]
                    for idx2 in range(idx1+1, len(coords)):
                        x2, y2 = coords[idx2]
                        dx, dy = x2-x1, y2-y1

                        nx, ny = x2, y2
                        while 0 <= nx < self.M and 0 <= ny < self.N:
                            antinodes.add((nx, ny))
                            nx, ny = nx+dx, ny+dy
                        
                        nx, ny = x1, y1
                        while 0 <= nx < self.M and 0 <= ny < self.N:
                            antinodes.add((nx, ny))
                            nx, ny = nx-dx, ny-dy
        
        return len(antinodes)


if __name__ == '__main__':
    sol = Solution('input1')
    print(sol.count_locations())
