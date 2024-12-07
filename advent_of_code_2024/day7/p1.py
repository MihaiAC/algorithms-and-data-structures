import re
from typing import List, Tuple

class Solution:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.pattern = re.compile("[0-9]+")

    def line_to_numbers(self, line: str) -> Tuple[int, List[int]]:
        str_nums = self.pattern.findall(line)
        return int(str_nums[0]), [int(x) for x in str_nums[1:]]

    # O(2*N), only works if the inputs are relatively small.
    def is_possible(self, target: int, nums: List[int]) -> bool:
        curr_partials = set([nums[0]])
        for num in nums[1:]:
            next_partials = set()
            for partial in curr_partials:
                if num + partial <= target:
                    next_partials.add(num+partial)
                
                if num * partial <= target:
                    next_partials.add(num*partial)
            curr_partials = next_partials
        return target in curr_partials


    def calculate_calibration_result(self):
        calibration_result = 0
        with open(self.input_file) as f:
            for line in f:
                if line != '\n':
                    target, nums = self.line_to_numbers(line)
                    if self.is_possible(target, nums):
                        calibration_result += target
        return calibration_result

if __name__ == '__main__':
    sol = Solution("input1")
    print(sol.calculate_calibration_result())