from collections import defaultdict
from tqdm import tqdm

class Solution:
    MODN = 2**24

    def __init__(self, input_file: str, steps: int):
        self.steps = steps

        if self.steps < 4:
            raise ValueError('Cannot have fewer than four steps.')
        
        self.deltas_to_vals = defaultdict(int)
        str_inputs = open(input_file).read().strip().split('\n')
        self.nums = [int(x) for x in str_inputs]

    @staticmethod
    def step(num: int) -> int:
        num = ((num << 6) ^ num) % Solution.MODN
        num = ((num >> 5) ^ num) % Solution.MODN
        num = ((num << 11) ^ num) % Solution.MODN
        return num

    def expand_num_and_add_to_deltas(self, num: int):
        local_deltas_to_vals = dict()
        calc_delta = lambda n, n1, n2, n3, n4: (n1%10-n%10, n2%10-n1%10, n3%10-n2%10, n4%10-n3%10)
        
        num1 = Solution.step(num)
        num2 = Solution.step(num1)
        num3 = Solution.step(num2)
        num4 = Solution.step(num3)

        delta = calc_delta(num, num1, num2, num3, num4)
        local_deltas_to_vals[delta] = num4 % 10
        
        for _ in range(self.steps-3):
            num, num1, num2, num3, num4 = num1, num2, num3, num4, Solution.step(num4)
            delta = calc_delta(num, num1, num2, num3, num4)
            if delta not in local_deltas_to_vals:
                local_deltas_to_vals[delta] = num4 % 10
        
        for delta, val in local_deltas_to_vals.items():
            self.deltas_to_vals[delta] += val
        return num
    
    def calc_optimal_delta_and_sum(self) -> int:
        optimal_delta = None
        max_sum = -1
        
        for num in tqdm(self.nums):
            self.expand_num_and_add_to_deltas(num)
        
        for delta, curr_sum in tqdm(self.deltas_to_vals.items()):
            if curr_sum > max_sum:
                max_sum = curr_sum
                optimal_delta = delta
        
        print(len(self.deltas_to_vals))
        print(optimal_delta)
        return max_sum


if __name__ == '__main__':
    sol = Solution('input', 2000)
    print(sol.calc_optimal_delta_and_sum())