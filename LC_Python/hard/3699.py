from functools import cache

MODN = 10**9 + 7


class Solution:
    def zigZagArrays(self, n: int, left: int, right: int) -> int:

        @cache
        def dp(idx, monotonicity, curr_val):
            if idx == 0:
                return 1
            if monotonicity == -1:
                return (
                    sum(
                        dp(idx - 1, 1, next_val)
                        for next_val in range(curr_val + 1, right + 1)
                    )
                    % MODN
                )
            else:
                return (
                    sum(dp(idx - 1, -1, next_val) for next_val in range(left, curr_val))
                    % MODN
                )

        return (
            sum(
                dp(n - 1, monotonicity, v)
                for monotonicity in (1, -1)
                for v in range(left, right + 1)
            )
            % MODN
        )


sol = Solution()
print(sol.zigZagArrays(3, 4, 5))
print(sol.zigZagArrays(3, 1, 3))
