from typing import Tuple, List
from collections import deque, defaultdict

class Solution:
    def __init__(self, input_file: str):
        self.matrix = open(input_file).read().strip().split('\n')
        self.nrows = len(self.matrix)
        self.ncols = len(self.matrix[0])

        self.init_start_and_end()
        self.DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
    @staticmethod
    def manhattan_dist(x: Tuple[int, int], y: Tuple[int, int]) -> int:
        return abs(x[0]-y[0]) + abs(x[1]-y[1])

    def init_start_and_end(self):
        found = 0
        for ii in range(self.nrows):
            for jj in range(self.ncols):
                if found == 2:
                    return
                
                if self.matrix[ii][jj] == 'E':
                    self.end = (ii, jj)
                    found += 1
                
                if self.matrix[ii][jj] == 'S':
                    self.start = (ii, jj)
                    found += 1
    
    def compute_distance_to(self, coords: Tuple[int, int]) -> List[List[int]]:
        min_dist = [[float('inf') for _ in range(self.ncols)] for _ in range(self.nrows)]
        curr_dist = 0
        queue = deque([coords])
        while len(queue) > 0:
            for _ in range(len(queue)):
                cx, cy = queue.pop()
                min_dist[cx][cy] = curr_dist
                for dx, dy in self.DELTAS:
                    if 0 <= cx+dx < self.nrows and 0 <= cy+dy < self.ncols and self.matrix[cx+dx][cy+dy] != '#' and min_dist[cx+dx][cy+dy] == float('inf'):
                        queue.appendleft((cx+dx, cy+dy))
                
            curr_dist += 1
        return min_dist

    def print_dist_matrix(self, dist: List[List[int]], output_file_name: str):
        with open(output_file_name, 'w+') as f:
            f.write('   ')
            for num in range(self.ncols):
                if num < 10:
                    f.write(' ' + str(num) + '  ')
                else:
                    f.write(' ' + str(num) + ' ')
            f.write('\n')
            for line_idx, line in enumerate(dist):
                if line_idx < 10:
                    f.write(str(line_idx) + '  ')
                else:
                    f.write(str(line_idx) + ' ')
                for num in line:
                    if num == float('inf'):
                        f.write(' ## ')
                    else:
                        if num < 10:
                            f.write(' ' + str(num) + '  ')
                        else:
                            f.write(' ' + str(num) + ' ')
                f.write('\n')

    
    # Return number of shortcuts that save >= threshold time.
    def calculate_n_shortcuts(self, threshold: int, max_cheat_dist: int) -> int:
        fx, fy = self.end

        dist_to_end = self.compute_distance_to((fx, fy))

        # Debugging.
        # self.print_dist_matrix(dist_to_end, 'debug_output_p1_1')

        shortcuts = set()
        shortcut_len_count = defaultdict(list)

        for ii in range(self.nrows):
            for jj in range(self.ncols):
                if self.matrix[ii][jj] == '#':
                    continue
                for dx in range(-max_cheat_dist, max_cheat_dist+1):
                    for dy in range(-(max_cheat_dist-abs(dx)), (max_cheat_dist-abs(dx)+1)):
                        nx = ii+dx
                        ny = jj+dy
                        if 0 <= nx < self.nrows and 0 <= ny < self.ncols and self.matrix[nx][ny] != '#':
                            old_dist = dist_to_end[ii][jj]
                            new_dist = Solution.manhattan_dist((ii, jj), (nx, ny)) + dist_to_end[nx][ny]
                            saved_dist = old_dist - new_dist
                            if saved_dist >= threshold:
                                shortcuts.add((ii, jj, nx, ny))
                                shortcut_len_count[saved_dist].append((ii, jj, nx, ny))
        
        print([(key, len(shortcut_len_count[key])) for key in sorted(shortcut_len_count.keys(), reverse=True)])
        return len(shortcuts)


        

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_n_shortcuts(100, 20))