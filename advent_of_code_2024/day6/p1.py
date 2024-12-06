from typing import Tuple

class Solution:
    def __init__(self, input_file: str):
        self.map = []
        with open(input_file) as f:
            for line in f:
                if line != '\n':
                    self.map.append(list(line[:-1]))
        self.nrows = len(self.map)
        self.ncols = len(self.map[0])
        
        self.MARK_TO_DIR = {'>': (0,1),
                            'v': (1,0),
                            '<': (0,-1),
                            '^': (-1,0)}
        self.DIR_TO_MARK = {(0,1): '>',
                            (1,0): 'v',
                            (0,-1): '<',
                            (-1,0): '^'}
        self.MARKS = {'>','<','^','v'}
        self.ROTATE = {(0,1): (1,0), (1,0): (0,-1), (0,-1): (-1,0), (-1,0): (0,1)}

    # For debuggging.
    def print_curr_state(self, cx: int, cy: int, cdir: Tuple[int, int]):
        aux = self.map[cx][cy]
        self.map[cx][cy] = self.DIR_TO_MARK[cdir]
        for line in self.map:
            print("".join(line))
        print("")
        self.map[cx][cy] = aux
    
    def calculate_n_visited(self) -> int:
        # Keep track of each visited cell and the direction of mvmt.
        # Repeat => we're in a loop.
        visited = set()
        n_visited = 0

        # Find start position and initial direction:
        for ii in range(self.nrows):
            for jj in range(self.ncols):
                if self.map[ii][jj] in self.MARKS:
                    cx, cy = ii, jj
                    cdir = self.MARK_TO_DIR[self.map[ii][jj]]
                    self.map[ii][jj] = '.'
        
        while True:
            # self.print_curr_state(cx, cy, cdir)
            if (cx, cy, cdir) in visited:
                break

            if self.map[cx][cy] == '.':
                self.map[cx][cy] = 'X'
                n_visited += 1
            
            visited.add((cx, cy, cdir))

            nx, ny = cx+cdir[0], cy+cdir[1]
            if nx < 0 or nx == self.nrows or ny < 0 or ny == self.ncols:
                break
            elif self.map[nx][ny] == '#':
                cdir = self.ROTATE[cdir]
            else:
                cx, cy = nx, ny

        return n_visited


if __name__ == '__main__':
    sol = Solution("input1")
    print(sol.calculate_n_visited())
