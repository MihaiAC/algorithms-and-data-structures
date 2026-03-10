import re

class Solution:
    def __init__(self, input_file):
        self.lines = []
        with open(input_file) as f:
            for line in f:
                if line != '\n':
                    self.lines.append(line[:-1])

    def calculate_sum(self) -> int:
        pattern = re.compile("-?[0-9]+")
        total_sum = 0
        for line in self.lines:
            nums = [int(x) for x in pattern.findall(line)]
            total_sum += sum(nums)
        return total_sum


if __name__ == '__main__':
    sol = Solution("input")
    print(sol.calculate_sum())
