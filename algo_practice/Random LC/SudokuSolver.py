from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        possible = dict()
        for ii in range(9):
            for jj in range(9):
                if board[ii][jj] == ".":
                    possible[(ii, jj)] = list(range(1, 10))

        def update_possible(ii: int, jj: int, number: int):
            for kk in range(9):
                if board[kk][jj] == "." and number in possible[(kk, jj)]:
                    possible[(kk, jj)].remove(number)
                    
                if board[ii][kk] == "." and number in possible[(ii, kk)]:
                    possible[(ii, kk)].remove(number)
                    
            for kk in range((ii//3)*3, (ii//3)*3+3):
                for ll in range((jj//3)*3, (jj//3)*3+3):
                    if board[kk][ll] == "." and number in possible[(kk, ll)]:
                        possible[(kk, ll)].remove(number)

        for ii in range(9):
            for jj in range(9):
                if board[ii][jj] != ".":
                    number = int(board[ii][jj])
                    update_possible(ii, jj, number)
        self.possible = possible
        
        print(self.possible)
        print(self.solve_sudoku_aux(board, len(possible)))
    
    def solve_sudoku_aux(self, board: List[List[str]], unfilled: int) -> bool:
        if unfilled == 0:
            return True

        for ii in range(9):
            for jj in range(9):
                if board[ii][jj] == ".":
                    for val in self.possible[(ii, jj)]:

                        if not self.check_board(board, val, ii, jj):
                            continue

                        board[ii][jj] = str(val)
                        if self.solve_sudoku_aux(board, unfilled-1):
                            return True
                    
                    board[ii][jj] = "."

                    return False

    def check_board(self, board: List[List[str]], number: int, row: int, col: int) -> bool:
        number = str(number)
        
        for ii in range(9):
            if board[row][ii] == number:
                return False
            elif board[ii][col] == number:
                return False
        
        ii = (row // 3) * 3
        jj = (col // 3) * 3
        for dx in range(3):
            for dy in range(3):
                if board[ii+dx][jj+dy] == number:
                    return False
        
        return True

        

if __name__ == '__main__':
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sol.solveSudoku(board)
    print(board)
