from itertools import accumulate

MODN = 10**9 + 7


class Solution:
    def zigZagArrays(self, n: int, left: int, right: int) -> int:
        # left..right is same as 0..right-left+1
        m = right - left + 1

        dp_prev_desc = [1] * m
        dp_prev_inc = [1] * m

        for _ in range(n - 1):
            sum_prev_desc = list(accumulate(dp_prev_desc, initial=0))
            sum_prev_inc = list(accumulate(dp_prev_inc, initial=0))

            dp_prev_desc = [x % MODN for x in sum_prev_inc[:-1]]

            sum_prev_desc_0_to_m = sum_prev_desc[-1]
            dp_prev_inc = [(sum_prev_desc_0_to_m - x) % MODN for x in sum_prev_desc[1:]]

        return (sum(dp_prev_desc) + sum(dp_prev_inc)) % MODN


sol = Solution()
print(sol.zigZagArrays(3, 4, 5))
print(sol.zigZagArrays(3, 1, 3))
