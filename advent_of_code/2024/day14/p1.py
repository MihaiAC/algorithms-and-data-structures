import re
from typing import List, Tuple

class Solution:
    def __init__(self, input_file: str):
        self.start_locations = []
        self.velocities = []
        
        pattern = re.compile(r"p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)")
        with open(input_file) as f:
            for line in f:
                vals = pattern.findall(line)[0]
                self.start_locations.append((int(vals[0]), int(vals[1])))
                self.velocities.append((int(vals[2]), int(vals[3])))
        
        self.TIME = 100
        if input_file == 'test':
            self.X = 11
            self.Y = 7
        else:
            self.X = 101
            self.Y = 103
    
    def calculate_final_positions(self) -> List[Tuple[int, int]]:
        final_positions = []
        for idx in range(len(self.start_locations)):
            sx, sy = self.start_locations[idx]
            vx, vy = self.velocities[idx]
            fx, fy = (sx + vx * self.TIME) % self.X, (sy + vy * self.TIME) % self.Y
            final_positions.append((fx, fy))
        return final_positions
    
    def calculate_safety_factor(self) -> int:
        '''
        q1 | q2
        -------
        q3 | q4
        '''
        final_positions = self.calculate_final_positions()
        q1, q2, q3, q4 = 0, 0, 0, 0
        x_thresh, y_thresh = self.X//2, self.Y//2
        for fx, fy in final_positions:
            if fx < x_thresh:
                if fy < y_thresh:
                    q1 += 1
                elif fy > y_thresh:
                    q3 += 1
            elif fx > x_thresh:
                if fy < y_thresh:
                    q2 += 1
                elif fy > y_thresh:
                    q4 += 1
        return q1 * q2 * q3 * q4

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_safety_factor())