from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [[], [], []]
        for ii in range(9):
            new_set = set()
            squares[ii//3].append(new_set)
        
        rows = []
        for ii in range(9):
            new_set = set()
            rows.append(new_set)
        
        cols = []
        for ii in range(9):
            new_set = set()
            cols.append(new_set)
        
        for ii in range(9):
            for jj in range(9):
                if board[ii][jj] == ".":
                    continue
                
                val = int(board[ii][jj])
                if val in rows[ii]:
                    return False
                
                if val in cols[jj]:
                    return False
                
                if val in squares[ii//3][jj//3]:
                    return False
                
                rows[ii].add(val)
                cols[jj].add(val)
                squares[ii//3][jj//3].add(val)
        
        return True

if __name__ == '__main__':
    sol = Solution()
    board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board))