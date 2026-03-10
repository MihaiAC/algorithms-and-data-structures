from p2 import Solution
from reddit_sol import part2
from random import randint, sample
from tqdm import tqdm

NROWS = 100
NCOLS = 100
NTRIALS = 100
# DELTAS = [(-1, 0), (0, 1), (0, -1), (-1, 0)]
DELTAS = [(0, 1), (0, -1), (1, 0)]

def generate_map():
    matrix = [['.' for _ in range(NCOLS)] for _ in range(NROWS)]
    # Add the outer walls.
    for row in range(NROWS):
        matrix[row][0] = '#'
        matrix[row][NCOLS-1] = '#'
    
    for col in range(NCOLS):
        matrix[0][col] = '#'
        matrix[NROWS-1][col] = '#'
    
    # Add the start and end.
    matrix[1][1] = 'S'
    matrix[NROWS-2][NCOLS-2] = 'E'

    not_visited = set()
    for row in range(1, NROWS-1):
        for col in range(1, NCOLS-1):
            not_visited.add((row, col))
    not_visited.remove((NROWS-2, NCOLS-2))

    # Generate a random walk from 'S' to 'E'.
    cx, cy = 1, 1
    while (cx, cy) != (NROWS-2, NCOLS-2):
        not_visited.discard((cx, cy))
        dx, dy = DELTAS[randint(0, len(DELTAS)-1)]
        while cx+dx in [0, NROWS-1] or cy+dy in [0, NCOLS-1]:
            dx, dy = DELTAS[randint(0, len(DELTAS)-1)]
        cx += dx
        cy += dy
    
    not_visited = list(not_visited)
    for cx, cy in sample(not_visited, len(not_visited)//2):
        matrix[cx][cy] = '#'
    
    return '\n'.join(["".join(row) for row in matrix])

for _ in tqdm(range(NTRIALS)):
    matrix = generate_map()
    open('generated_input', 'w+').write(matrix)
    
    sol = Solution('generated_input')
    n_tiles_my_sol = sol.calc_n_tiles()

    n_tiles_internet_sol = part2('generated_input')

    if n_tiles_my_sol != n_tiles_internet_sol:
        print("ES.EYCH.AI.TEE")
        break

print('Done.')