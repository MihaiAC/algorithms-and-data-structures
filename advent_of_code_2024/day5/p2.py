from collections import defaultdict
from functools import cmp_to_key
from typing import List

class Solution:
    def __init__(self, input_file):
        self.greater_than = defaultdict(list)
        self.lists = []
        with open(input_file) as f:
            for line in f:
                line = line[:-1]
                if '|' in line:
                    numbers = line.split('|')
                    self.greater_than[int(numbers[0])].append(int(numbers[1]))
                elif line == '':
                    continue
                else:
                    self.lists.append([int(x) for x in line.split(",")])

    def validate_list(self, nums: List[int]) -> bool:
        prev = set()
        for num in nums:
            for smaller_num in self.greater_than[num]:
                if smaller_num in prev:
                    return False
            prev.add(num)
        return True

    def comparator(self, num1: int, num2: int) -> int:
        if num2 in self.greater_than[num1]:
            return 1
        elif num1 in self.greater_than[num2]:
            return -1
        return 0

    def calculate_sum(self) -> int:
        sum_of_middles = 0
        for nums in self.lists:
            if not self.validate_list(nums):
                nums.sort(key=cmp_to_key(self.comparator))
                sum_of_middles += nums[len(nums)//2]
        return sum_of_middles

if __name__ == '__main__':
    sol = Solution("test1")
    print(sol.calculate_sum())
