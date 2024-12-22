class Solution:
    MODN = 2**24

    def __init__(self, input_file: str):
        str_inputs = open(input_file).read().strip().split('\n')
        self.nums = [int(x) for x in str_inputs]

    @staticmethod
    def step(num: int) -> int:
        num = ((num << 6) ^ num) % Solution.MODN
        num = ((num >> 5) ^ num) % Solution.MODN
        num = ((num << 11) ^ num) % Solution.MODN
        return num


    @staticmethod
    def expand_num(num: int, times: int) -> int:
        for _ in range(times):
            num = Solution.step(num)
        return num
    
    def calc_sum(self, times: int) -> int:
        res = 0
        for num in self.nums:
            res += Solution.expand_num(num, times)
        return res


if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calc_sum(2000))