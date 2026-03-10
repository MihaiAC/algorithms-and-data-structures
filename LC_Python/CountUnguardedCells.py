from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unguarded = m*n

        UNGUARDED = 0
        GUARDED = 1
        WALL = 2
        GUARD = 3

        
        matrix = [[UNGUARDED for _ in range(n)] for _ in range(m)]
        for rw, cw in walls:
            matrix[rw][cw] = WALL
        
        for rg, cg in guards:
            matrix[rg][cg] = GUARD

        for guard_row, guard_col in guards:
            for current_col in range(guard_col-1, -1, -1):
                if matrix[guard_row][current_col] in [WALL, GUARD]:
                    break
                elif matrix[guard_row][current_col] == UNGUARDED:
                    matrix[guard_row][current_col] = GUARDED
            
            for current_col in range(guard_col+1, n):
                if matrix[guard_row][current_col] in [WALL, GUARD]:
                    break
                elif matrix[guard_row][current_col] == UNGUARDED:
                    matrix[guard_row][current_col] = GUARDED
            
            for current_row in range(guard_row-1, -1, -1):
                if matrix[current_row][guard_col] in [WALL, GUARD]:
                    break
                elif matrix[current_row][guard_col] == UNGUARDED:
                    matrix[current_row][guard_col] = GUARDED
            
            for current_row in range(guard_row+1, m):
                if matrix[current_row][guard_col] in [WALL, GUARD]:
                    break
                elif matrix[current_row][guard_col] == UNGUARDED:
                    matrix[current_row][guard_col] = GUARDED
        
        unguarded = 0
        for ii in range(m):
            for jj in range(n):
                if matrix[ii][jj] == UNGUARDED:
                    unguarded += 1

        return unguarded