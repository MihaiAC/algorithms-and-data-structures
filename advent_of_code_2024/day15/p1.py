import tkinter as tk
import time
from typing import Tuple

class Solution:
    def __init__(self, input_file: str, plot: bool):
        input_lines = open(input_file).read().strip().split('\n')
        sep_idx = input_lines.index('')
        
        # Initialise matrix and the list of moves.
        self.matrix = [list(x) for x in input_lines[:sep_idx]]
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

    def calculate_score(self) -> int:
        score = 0
        for ii in range(self.nrows):
            for jj in range(self.ncols):
                if self.matrix[ii][jj] == 'O':
                    score += 100*ii+jj
        return score
    
    # Return new coordinates after making the move.
    def make_move_return_new_pos(self, cx: int, cy: int, delta: Tuple[int, int]) -> Tuple[int, int]:
        dx, dy = delta
        nx, ny = cx+dx, cy+dy
        
        if self.matrix[nx][ny] == '#':
            return (cx, cy)
        elif self.matrix[nx][ny] == '.':
            self.matrix[nx][ny] = '@'
            self.matrix[cx][cy] = '.'

            # Update tkinter image.
            if self.plot:
                self.labels[cx][cy].config(text='.')
                self.labels[nx][ny].config(text='@')
            
            return (nx, ny)
        else:
            ix, iy = nx, ny
            while self.matrix[ix][iy] not in ['.', '#']:
                ix += dx
                iy += dy
            
            # Move not possible, line of boxes stacked to a wall.
            if self.matrix[ix][iy] == '#':
                return (cx, cy)
            
            self.matrix[ix][iy] = 'O'
            self.matrix[nx][ny] = '@'
            self.matrix[cx][cy] = '.'

            # Update tkinter image.
            if self.plot:
                self.labels[ix][iy].config(text='O')
                self.labels[nx][ny].config(text='@')
                self.labels[cx][cy].config(text='.')

            return (nx, ny)

    def move_boxes(self):
        cx, cy = self.find_starting_pos()
        for move_row in self.moves:
            for move in move_row:
                cx, cy = self.make_move_return_new_pos(cx, cy, self.DELTAS[move])
                # print(f"{cx, cy}")
                if self.plot:
                    self.root.update()
                    time.sleep(0.01)


if __name__ == '__main__':
    sol = Solution('input', False)
    sol.move_boxes()
    print(sol.calculate_score())
    
    if sol.plot:
        sol.root.destroy()
