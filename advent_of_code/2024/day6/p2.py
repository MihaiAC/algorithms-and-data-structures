from typing import Tuple
from copy import deepcopy
from tqdm import tqdm

class Solution:
    def __init__(self, input_file: str):
        self.initialise_map(input_file)
        self.initialise_constants()
        self.initialise_start()

    
    def initialise_map(self, input_file: str):
        self.map = []
        with open(input_file) as f:
            for line in f:
                if line != '\n':
                    self.map.append(list(line[:-1]))
        self.nrows = len(self.map)
        self.ncols = len(self.map[0])
    
    def initialise_constants(self):
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

    # Find start position and initial direction.
    def initialise_start(self):
        for ii in range(self.nrows):
            for jj in range(self.ncols):
                if self.map[ii][jj] in self.MARKS:
                    self.x_start = ii
                    self.y_start = jj
                    self.cdir_start = self.MARK_TO_DIR[self.map[ii][jj]]
                    self.map[ii][jj] = '.'

    # For debuggging.
    def print_curr_state(self, cx: int, cy: int, cdir: Tuple[int, int]):
        aux = self.map[cx][cy]
        self.map[cx][cy] = self.DIR_TO_MARK[cdir]
        for line in self.map:
            print("".join(line))
        print("")
        self.map[cx][cy] = aux
    
    # Slight improvement: only consider coords on the normal route for 
    # obstacle placement.
    def calculate_n_obstacles(self) -> int:
        n_obstacles = 0
        map_original = deepcopy(self.map)
        
        # We know that the initial input is not a loop, but just in case.
        if self.is_loop():
            return -1
        
        normal_route = deepcopy(self.map)
        for ii in tqdm(range(self.nrows)):
            for jj in tqdm(range(self.ncols)):
                if normal_route[ii][jj] == 'X' and (ii != self.x_start or jj != self.y_start):
                    self.map = deepcopy(map_original)
                    self.map[ii][jj] = '#'
                    if self.is_loop():
                        n_obstacles += 1
        return n_obstacles


    def is_loop(self) -> bool:
        # Keep track of each visited cell and the direction of mvmt.
        # Repeat => we're in a loop.
        visited = set()
        
        cx, cy = self.x_start, self.y_start
        cdir = self.cdir_start
        
        while True:
            # self.print_curr_state(cx, cy, cdir)
            if (cx, cy, cdir) in visited:
                return True

            if self.map[cx][cy] == '.':
                self.map[cx][cy] = 'X'
            
            visited.add((cx, cy, cdir))

            nx, ny = cx+cdir[0], cy+cdir[1]
            if nx < 0 or nx == self.nrows or ny < 0 or ny == self.ncols:
                return False
            elif self.map[nx][ny] == '#':
                cdir = self.ROTATE[cdir]
            else:
                cx, cy = nx, ny
        


if __name__ == '__main__':
    sol = Solution("input1")
    print(sol.calculate_n_obstacles())
