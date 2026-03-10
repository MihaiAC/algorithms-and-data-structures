from typing import List, Tuple, Set

class Solution:
    def check_if_possible(self, board:List[List[str]], word:str) -> bool:
        board_letters = set()
        word_letters = set()

        for ii in range(self.nrows):
            for jj in range(self.ncols):
                board_letters.add(board[ii][jj])
        
        for ii in range(len(word)):
            word_letters.add(word[ii])

        if len(word_letters.difference(board_letters)) > 0:
            return False
        
        return True

    def df_search_word(self, board:List[List[str]], word:str, start:Tuple[int, int], idx:int, used:Set[Tuple[int, int]]) -> bool:
        if idx == len(word):
            return True
        
        sx, sy = start
        for x, y in [(sx+1, sy), (sx-1, sy), (sx, sy+1), (sx, sy-1)]:
            if x < 0 or x >= self.nrows or y < 0 or y >= self.ncols:
                continue
            if (x, y) in used:
                continue
            if board[x][y] == word[idx]:
                used.add((x, y))
                if self.df_search_word(board, word, (x, y), idx+1, used):
                    return True
                else:
                    used.remove((x, y))
                    continue
            else:
                continue

        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.nrows = len(board)
        self.ncols = len(board[0])

        if not self.check_if_possible(board, word):
            return False

        for ii in range(self.nrows):
            for jj in range(self.ncols):
                if board[ii][jj] == word[0]:
                    if self.df_search_word(board, word, (ii, jj), 1, set([(ii, jj)])):
                        return True
        
        return False

if __name__ == '__main__':
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
    word = "SEE"
    print(sol.exist(board, word))
