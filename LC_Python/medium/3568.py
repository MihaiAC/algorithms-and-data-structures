from typing import List
from collections import deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        nrows = len(classroom)
        ncols = len(classroom[0])

        srow, scol = 0, 0
        litter_idx = dict()
        for row in range(nrows):
            for col in range(ncols):
                cell = classroom[row][col]
                if cell == "S":
                    srow, scol = row, col
                elif cell == "L":
                    litter_idx[(row, col)] = len(litter_idx)

        N_litter = len(litter_idx)
        if N_litter == 0:
            return 0

        full_mask = (1 << N_litter) - 1

        # best[row][col][mask] = x => the most energy we can have standing on
        # (row, col) with the litter in mask collected.
        best = [[[-1] * (full_mask + 1) for _ in range(ncols)] for _ in range(nrows)]
        best[srow][scol][0] = energy

        queue = deque()
        queue.append((srow, scol, 0, energy))

        moves = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                curr_row, curr_col, curr_mask, curr_energy = queue.popleft()

                if curr_mask == full_mask:
                    return moves

                if curr_energy == 0:
                    continue

                for row, col in [
                    (curr_row + 1, curr_col),
                    (curr_row - 1, curr_col),
                    (curr_row, curr_col + 1),
                    (curr_row, curr_col - 1),
                ]:
                    if row < 0 or row >= nrows or col < 0 or col >= ncols:
                        continue

                    cell = classroom[row][col]
                    if cell == "X":
                        continue

                    mask = curr_mask
                    if cell == "L":
                        mask |= 1 << litter_idx[(row, col)]

                    new_energy = energy if cell == "R" else curr_energy - 1
                    if new_energy <= best[row][col][mask]:
                        continue

                    best[row][col][mask] = new_energy
                    queue.append((row, col, mask, new_energy))

            moves += 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMoves(["S.", "XL"], 2))
    print(sol.minMoves(["LS", "RL"], 4))
    print(sol.minMoves(["L.S", "RXL"], 3))
    print(sol.minMoves(["S", "X", "L"], 5))
