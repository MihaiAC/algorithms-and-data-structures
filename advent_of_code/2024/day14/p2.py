import re
import matplotlib.pyplot as plt
import heapq
from tqdm import tqdm
from copy import deepcopy

class Solution:
    def __init__(self, input_file: str):
        self.x_coords = []
        self.y_coords = []
        self.velocities = []
        
        pattern = re.compile(r"p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)")
        with open(input_file) as f:
            for line in f:
                vals = pattern.findall(line)[0]
                self.x_coords.append(int(vals[0]))
                self.y_coords.append(int(vals[1]))
                self.velocities.append((int(vals[2]), int(vals[3])))
        
        self.N = len(self.x_coords)
        self.X = 101
        self.Y = 103
        
        self.MAXITER = 100000
        self.HEAP_SIZE = 20
    
    def calculate_and_print_lowest_safety_factors(self) -> None:
        max_heap = []
        for iteration in tqdm(range(1, self.MAXITER+1)):
            for idx in range(self.N):
                self.x_coords[idx] = (self.x_coords[idx] + self.velocities[idx][0]) % self.X
                self.y_coords[idx] = (self.y_coords[idx] + self.velocities[idx][1]) % self.Y
            
            if len(max_heap) < self.HEAP_SIZE:
                heapq.heappush(max_heap, (-self.calculate_safety_factor(), iteration, deepcopy(self.x_coords), deepcopy(self.y_coords)))
            else:
                safety_factor = -self.calculate_safety_factor()
                if safety_factor > max_heap[0][0]:
                    heapq.heappushpop(max_heap, (safety_factor, iteration, deepcopy(self.x_coords), deepcopy(self.y_coords)))
        
        while len(max_heap) > 0:
            safety_factor, iteration, X, Y = heapq.heappop(max_heap)
            plt.scatter(X, Y, c="black")
            plt.savefig("Iteration " + str(iteration) + " safety_factor=" + str(-safety_factor))
            plt.clf()
    
    def calculate_safety_factor(self) -> int:
        '''
        q1 | q2
        -------
        q3 | q4
        '''
        q1, q2, q3, q4 = 0, 0, 0, 0
        x_thresh, y_thresh = self.X//2, self.Y//2
        for idx in range(self.N):
            fx = self.x_coords[idx]
            fy = self.y_coords[idx]
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
    print(sol.calculate_and_print_lowest_safety_factors())