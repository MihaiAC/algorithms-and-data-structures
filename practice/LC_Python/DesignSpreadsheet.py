from collections import defaultdict

class Spreadsheet:
    def __init__(self, rows: int):
        self.table = defaultdict(dict)

    def setCell(self, cell: str, value: int) -> None:
        letter = cell[0]
        row = int(cell[1:])
        self.table[letter][row] = value

    def resetCell(self, cell: str) -> None:
        letter = cell[0]
        row = int(cell[1:])
        self.table[letter][row] = 0
        

    def getValue(self, formula: str) -> int:
        elems = formula[1:].split('+')
        ans = 0
        for elem in elems:
            if elem[0].isalpha():
                letter = elem[0]
                row = int(elem[1:])
                ans += self.table[letter].get(row, 0)
            else:
                ans += int(elem)
        return ans