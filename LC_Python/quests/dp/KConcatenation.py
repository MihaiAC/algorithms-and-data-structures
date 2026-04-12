from typing import List

MODN = 10**9 + 7


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # Calculate max prefix + total sum + inner sum.
        max_prefix = 0
        curr = 0

        curr_inner = 0
        best_inner = 0
        for num in arr:
            curr += num
            max_prefix = max(max_prefix, curr)

            curr_inner = max(num, curr_inner + num)
            best_inner = max(best_inner, curr_inner)

        total_sum = curr

        # Calculate max suffix.
        curr = 0
        max_suffix = 0
        for num in arr[::-1]:
            curr += num
            max_suffix = max(max_suffix, curr)

        # Trivial cases.
        ans = max(0, max_prefix, max_suffix, total_sum * k, best_inner)

        # At least one repeat =>
        if k > 1:
            ans = max(
                ans,
                max_prefix + total_sum * (k - 1),
                total_sum * (k - 1) + max_suffix,
                max_prefix + max_suffix,
            )

        if k > 2:
            ans = max(ans, (k - 2) * total_sum + max_suffix + max_prefix)

        return ans % MODN


sol = Solution()
print(sol.kConcatenationMaxSum([1, 2], 3))
print(sol.kConcatenationMaxSum([1, -2, 1], 5))
print(sol.kConcatenationMaxSum([-1, -2], 7))
