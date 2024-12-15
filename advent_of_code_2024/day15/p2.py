import tkinter as tk
import time
from typing import Tuple

class Solution:
    def __init__(self, input_file: str, plot: bool):
        input_lines = open(input_file).read().strip().split('\n')
        sep_idx = input_lines.index('')
        
        # Initialise matrix and the list of moves.
        self.matrix = [list(x) for x in input_lines[:sep_idx]]
        self.double_map()
        
        self.nrows = len(self.matrix)
        self.ncols = len(self.matrix[0])

        self.moves = input_lines[sep_idx+1:]

        # Map move symbols to corresponding movement.
        self.DELTAS = {
            '^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0),
            '<': (0, -1)
        }
        
        self.plot = plot

        if self.plot:
            # Init tkinter grid.
            self.init_tkinter()
    
    def double_map(self):
        for row_idx, row in enumerate(self.matrix):
            new_row = []
            for elem in row:
                if elem == '#':
                    new_row += ['#', '#']
                elif elem == '@':
                    new_row += ['@', '.']
                elif elem == 'O':
                    new_row += ['[', ']']
                else:
                    new_row += ['.', '.']
            self.matrix[row_idx] = new_row

    def init_tkinter(self):
        # Tkinter window
        self.root = tk.Tk()
        self.root.title("Dynamic 2D Array Display")
        self.root.configure(background='black')

        # Create a grid of labels to display the array
        self.labels = []
        for row_idx, row in enumerate(self.matrix):
            label_row = []
            for col_idx, value in enumerate(row):
                label = tk.Label(self.root, text=str(value), font=("Helvetica", 5), width=2, height=2,
                                 borderwidth=0, relief="solid", bg="black", fg="white")
                label.grid(row=row_idx, column=col_idx, padx=1, pady=1)
                label_row.append(label)
            self.labels.append(label_row)
    
    def find_starting_pos(self) -> Tuple[int, int]:
        for row_idx in range(self.nrows):
            for col_idx in range(self.ncols):
                if self.matrix[row_idx][col_idx] == '@':
                    return (row_idx, col_idx)
        
        raise ValueError("Input does not contain starting position.")
    
    def update_cell(self, cx: int, cy: int, value: str):
        self.matrix[cx][cy] = value
        if self.plot:
            self.labels[cx][cy].config(text=value)

    def calculate_score(self) -> int:
        score = 0
        for ii in range(self.nrows):
            for jj in range(self.ncols):
                if self.matrix[ii][jj] == '[':
                    score += 100*ii+jj
        return score
    
    # cx, cy corresponds to the left side of the box '['.
    def is_possible_move_box_vert(self, cx: int, cy: int, delta: Tuple[int, int]) -> bool:
        rscx, rscy = cx, cy+1
        dx, dy = delta
        rsnx, rsny = rscx+dx, rscy+dy
        nx, ny = cx+dx, cy+dy

        if self.matrix[nx][ny] == '#' or self.matrix[rsnx][rsny] == '#':
            return False
        
        if self.matrix[nx][ny] == '[' and self.is_possible_move_box_vert(nx, ny, delta):
            return True
        
        if self.matrix[nx][ny] == ']' and self.is_possible_move_box_vert(nx, ny-1, delta):
            # self.matrix[rsnx][rsny] can be '.' or '['. It cannot be '#', ']' or '@'.
            if self.matrix[rsnx][rsny] == '.' or (self.matrix[rsnx][rsny] == '[' and self.is_possible_move_box_vert(rsnx, rsny, delta)):
                return True
        
        if self.matrix[nx][ny] == '.':
            if self.matrix[rsnx][rsny] == '.' or (self.matrix[rsnx][rsny] == '[' and self.is_possible_move_box_vert(rsnx, rsny, delta)):
                return True
        return False
    
   
    # Called when we know the box can eventually be moved.
    def move_box_vert(self, cx: int, cy: int, delta: Tuple[int, int]):
        rscx, rscy = cx, cy+1
        dx, dy = delta
        rsnx, rsny = rscx+dx, rscy+dy
        nx, ny = cx+dx, cy+dy

        # First, move the boxes that are on top of the current box.
        if self.matrix[nx][ny] == '[':
            self.move_box_vert(nx, ny, delta)
        elif self.matrix[nx][ny] == ']':
            self.move_box_vert(nx, ny-1, delta)
        
        if self.matrix[rsnx][rsny] == '[':
            self.move_box_vert(rsnx, rsny, delta)
        
        # Now move the current box, space should be cleared up.
        self.update_cell(nx, ny, '[')
        self.update_cell(rsnx, rsny, ']')
        self.update_cell(cx, cy, '.')
        self.update_cell(rscx, rscy, '.')

    
    def move_box_vert_if_possible(self, cx: int, cy: int, delta: Tuple[int, int]) -> bool:
        self.cache = dict()
        if self.is_possible_move_box_vert(cx, cy, delta):
            self.move_box_vert(cx, cy, delta)
            return True
        return False

    
    def move_box_horiz_if_possible(self, cx: int, cy: int, delta: Tuple[int, int]) -> bool:
        ix, iy = cx, cy
        dx, dy = delta
        
        while self.matrix[ix][iy] not in ['.', '#']:
            ix += dx
            iy += dy
        
        if self.matrix[ix][iy] == '#':
            return False
        else:
            dx, dy = -dx, -dy
            while iy != cy:
                ny = iy+dy
                # self.matrix[ix][iy] = self.matrix[ix][ny]
                self.update_cell(ix, iy, self.matrix[ix][ny])
                iy = ny
            self.matrix[cx][cy] = '.'
            return True
    

    # Return the robot's new coordinates after making the move.
    def make_move_return_new_pos(self, cx: int, cy: int, delta: Tuple[int, int]) -> Tuple[int, int]:
        dx, dy = delta
        nx, ny = cx+dx, cy+dy
        
        if self.matrix[nx][ny] == '#':
            return (cx, cy)
        elif self.matrix[nx][ny] == '.':
            self.update_cell(nx, ny, '@')
            self.update_cell(cx, cy, '.')
            return (nx, ny)
        else:
            if dx == 0:
                # Moving horizontally.
                if self.matrix[nx][ny] == '[' and self.move_box_horiz_if_possible(nx, ny, delta):
                    self.update_cell(nx, ny, '@')
                    self.update_cell(cx, cy, '.')
                    return (nx, ny)
                elif self.matrix[nx][ny] == ']' and self.move_box_horiz_if_possible(nx, ny-1, delta):
                    self.update_cell(nx, ny-1, ']')
                    self.update_cell(nx, ny, '@')
                    self.update_cell(cx, cy, '.')
                    return (nx, ny)
                else:
                    return (cx, cy)
            else:
                # Moving vertically.
                if (self.matrix[nx][ny] == '[' and self.move_box_vert_if_possible(nx, ny, delta)) or (self.matrix[nx][ny] == ']' and self.move_box_vert_if_possible(nx, ny-1, delta)):
                    self.update_cell(nx, ny, '@')
                    self.update_cell(cx, cy, '.')
                    return (nx, ny)
                return (cx, cy)

    def move_boxes(self):
        cx, cy = self.find_starting_pos()
        for move_row in self.moves:
            for move in move_row:
                if self.plot:
                    nx, ny = self.make_move_return_new_pos(cx, cy, self.DELTAS[move])
                    if self.plot:
                        if cx == nx and cy == ny:
                            self.update_cell(cx, cy, move)
                            self.root.update()
                            time.sleep(0.7)
                            self.update_cell(cx, cy, '@')
                        self.root.update()
                        time.sleep(0.3)
                    cx, cy = nx, ny


if __name__ == '__main__':
    sol = Solution('input', True)
    sol.move_boxes()
    print(sol.calculate_score())
    
    if sol.plot:
        sol.root.destroy()
    
    print(sol.matrix)
