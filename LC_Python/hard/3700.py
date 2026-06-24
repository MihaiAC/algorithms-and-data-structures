import numpy as np

MODN = 10**9 + 7


class Solution:
    def zigZagArrays(self, n: int, left: int, right: int) -> int:
        m = right - left + 1

        if n == 1:
            return m % MODN

        idx = np.arange(m)
        # top-right block: 1 where row > col
        B = (idx[:, None] > idx[None, :]).astype(object)

        # bottom-left block: 1 where row < col
        A = (idx[:, None] < idx[None, :]).astype(object)

        zero = np.zeros((m, m), dtype=object)
        U = np.block([[zero, B], [A, zero]])

        dp_prev_desc = np.ones(m, dtype=object)
        dp_prev_inc = np.ones(m, dtype=object)
        dp = np.concatenate([dp_prev_desc, dp_prev_inc])[None]

        exp, base = n - 1, U
        while exp > 0:
            if exp & 1:
                dp = dp @ base % MODN
            base = base @ base % MODN
            exp >>= 1

        return int(dp.sum() % MODN)


sol = Solution()
print(sol.zigZagArrays(3, 4, 5))
print(sol.zigZagArrays(3, 1, 3))
print(sol.zigZagArrays(3254, 1, 25))
