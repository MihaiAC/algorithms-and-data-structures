from math import gcd


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # If t contains any prime factor that's not a digit, tough luck.
        aux = t
        for div in range(2, 10):
            while aux % div == 0:
                aux = aux // div

        if aux != 1:
            return "-1"

        # Go l->R, note down leftmost 0 and the product the remaining digits should have.
        N = len(num)

        rem = [0] * (N + 1)
        rem[0] = t

        leftmost_zero_idx = N - 1

        for idx, digit in enumerate(num):
            if digit == "0":
                leftmost_zero_idx = idx
                break

            rem[idx + 1] = rem[idx] // gcd(rem[idx], int(digit))

        if leftmost_zero_idx == N - 1 and rem[N] == 1:
            return num

        # Go R -> L from the leftmost zero, raising the pivot digit and
        # greedily filling everything after it (9 down to 1).
        num_list = list(num)
        for pivot_idx in range(leftmost_zero_idx, -1, -1):
            for pivot_digit in range(int(num_list[pivot_idx]) + 1, 10):
                num_list[pivot_idx] = str(pivot_digit)
                t_now = rem[pivot_idx] // gcd(rem[pivot_idx], pivot_digit)

                suffix_digit = 9
                for suffix_idx in range(N - 1, pivot_idx, -1):
                    while t_now % suffix_digit != 0:
                        suffix_digit -= 1
                    t_now //= suffix_digit
                    num_list[suffix_idx] = str(suffix_digit)

                if t_now == 1:
                    return "".join(num_list)

        # If no same length answer exists, greedily construct the answer
        # from t's factors (largest to the right) then pad with 1's as needed.
        ans = []
        original_t = t
        for div in range(9, 1, -1):
            while original_t % div == 0:
                ans.append(str(div))
                original_t //= div

        return "1" * max(N + 1 - len(ans), 0) + "".join(ans[::-1])


sol = Solution()
print(sol.smallestNumber("1234", 256))
print(sol.smallestNumber("12355", 50))
print(sol.smallestNumber("11111", 26))
