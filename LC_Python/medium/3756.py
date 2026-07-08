from typing import List

MODN = 10**9 + 7
MAX_LEN = 10**5

# Precompute pow 10's.
pow_10 = [1] * (MAX_LEN + 1)
for ii in range(1, MAX_LEN + 1):
    pow_10[ii] = pow_10[ii - 1] * 10 % MODN


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)

        pre_sum = [0] * (N + 1)
        pre_num = [0] * (N + 1)
        pre_cnt = [0] * (N + 1)

        for idx, ch in enumerate(s):
            digit = int(ch)

            pre_sum[idx + 1] = pre_sum[idx] + digit
            if digit > 0:
                pre_num[idx + 1] = (pre_num[idx] * 10 + digit) % MODN
                pre_cnt[idx + 1] = pre_cnt[idx] + 1
            else:
                pre_num[idx + 1] = pre_num[idx]
                pre_cnt[idx + 1] = pre_cnt[idx]

        ans = []
        for left, right in queries:
            # pre_num[left] = most significant digits that we need
            # to remove from pre_num[right+1]
            # So, we need to shift pre_num[left] left (base 10) by
            # the length of the number and subtract it from pre_num[right+1]
            # to get the actual reconstructed number.
            length = (
                pre_cnt[right + 1] - pre_cnt[left]
            )  # length of the number after removing 0s
            num = (
                pre_num[right + 1] - pow_10[length] * pre_num[left]
            )  # actual number (MOD whatever)
            digit_sum = pre_sum[right + 1] - pre_sum[left]
            ans.append((num * digit_sum) % MODN)

        return ans


sol = Solution()
print(sol.sumAndMultiply("10203004", [[0, 7], [1, 3], [4, 6]]))
print(sol.sumAndMultiply("1000", [[0, 3], [1, 1]]))
print(sol.sumAndMultiply("9876543210", [[0, 9]]))
