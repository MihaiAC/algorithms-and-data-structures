from typing import Tuple
from functools import cache


def calculate_waviness_up_to(num: int) -> int:
    """
    Calculates waviness from 0 up to and including num.
    """
    # Can't have a wavy number with 2 digits, and 100 isn't wavy.
    if num <= 100:
        return 0

    str_num = str(num)

    @cache
    def dfs(
        curr_idx: int,
        penultimate_digit: int,
        prev_digit: int,
        tight: bool,
        leading_zeros: bool,
    ) -> Tuple[int, int]:
        """
        curr_idx: Current idx we reached within the current number we're constructing.
        penultimate_digit: Digit at idx-2 within the current number, or -1 if not initialised.
        prev_digit: Digit at idx-1 within the current number, or -1.
        tight: Controls up to what number the current digit can go to.
        leading_zeros: True if the zeros preceding curr_idx are leading zeros.
        """
        if curr_idx == len(str_num):
            return [1, 0]

        total_count = 0
        total_waviness = 0

        digit_limit = int(str_num[curr_idx]) if tight else 9

        if leading_zeros:
            count, waviness = dfs(
                curr_idx + 1, -1, -1, tight and digit_limit == 0, True
            )
            total_count += count
            total_waviness += waviness

        for curr_digit in range(digit_limit + 1):
            if curr_digit == 0 and leading_zeros:
                # Handled this in the conditional above.
                continue

            # Are we forming a new peak by adding curr_digit?
            peak = 0
            if (
                penultimate_digit != -1
                and prev_digit != -1
                and (
                    (prev_digit > penultimate_digit and prev_digit > curr_digit)
                    or (prev_digit < penultimate_digit and prev_digit < curr_digit)
                )
            ):
                peak = 1

            count, waviness = dfs(
                curr_idx + 1,
                prev_digit,
                curr_digit,
                tight and curr_digit == digit_limit,
                False,
            )

            total_count += count
            total_waviness += waviness + peak * count

        return [total_count, total_waviness]

    return dfs(0, -1, -1, True, True)[1]


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return calculate_waviness_up_to(num2) - calculate_waviness_up_to(num1 - 1)


sol = Solution()
print(sol.totalWaviness(120, 130))
print(sol.totalWaviness(198, 202))
print(sol.totalWaviness(4848, 4848))

print(calculate_waviness_up_to(101))
