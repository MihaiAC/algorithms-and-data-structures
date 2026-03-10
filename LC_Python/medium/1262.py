from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        plus_1 = []
        plus_2 = []
        total_sum = 0

        def append_to(x: int, plus: List[int]) -> List[int]:
            if len(plus) == 0:
                plus.append(x)
            elif len(plus) == 1:
                if x < plus[0]:
                    plus = [x, plus[0]]
                else:
                    plus.append(x)
            else:
                if x < plus[0]:
                    plus[0], plus[1] = x, plus[0]
                elif x < plus[1]:
                    plus[1] = x
            return plus

        for num in nums:
            total_sum += num

            if num % 3 == 1:
                plus_1 = append_to(num, plus_1)
            elif num % 3 == 2:
                plus_2 = append_to(num, plus_2)

        if total_sum % 3 == 0:
            return total_sum
        else:
            if total_sum % 3 == 1:
                sel_one, sel_two = plus_1, plus_2
            else:
                sel_one, sel_two = plus_2, plus_1

            max_sum = 0

            if len(sel_one) > 0:
                max_sum = max(max_sum, total_sum - sel_one[0])

            if len(sel_two) > 1:
                max_sum = max(max_sum, total_sum - sum(sel_two))

            return max_sum
