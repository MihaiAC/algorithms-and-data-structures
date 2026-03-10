from typing import List
from functools import cache

class Solution:
    def __init__(self, input_file: str):
        with open(input_file) as f:
            line = f.readline()
            self.init_nums = [int(x) for x in line.split(" ")]
        
        self.N_EXPANSIONS = 75
    
    @staticmethod
    def calculate_next_nums(num: int) -> List[int]:
        if num == 0:
            return [1]
        elif len(str(num)) % 2 == 0:
            str_num = str(num)
            return [int(str_num[:len(str_num)//2]), int(str_num[len(str_num)//2:])]
        else:
            return [2024*num]
    
    @cache
    @staticmethod
    def expand_num_return_count(num: int, expansions_left: int) -> int:
        if expansions_left:
            next_nums = Solution.calculate_next_nums(num)
            count = 0
            for next_num in next_nums:
                count += Solution.expand_num_return_count(next_num, expansions_left-1)
            return count
        return 1

    def calculate_n_stones(self) -> int:
        n_stones = 0
        for num in self.init_nums:
            n_stones += Solution.expand_num_return_count(num, self.N_EXPANSIONS)
        return n_stones


if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calculate_n_stones())
