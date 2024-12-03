import re

class Solution:
    def calc_result(self, input_file: str) -> int:
        pattern_1 = re.compile(r'mul\([0-9]+,[0-9]+\)')
        pattern_2 = re.compile(r'[0-9]+')
        answer = 0
        with open(input_file) as f:
            for line in f:
                for mul in pattern_1.findall(line):
                    nums = pattern_2.findall(mul)
                    answer += int(nums[0]) * int(nums[1])
        return answer
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.calc_result("input"))