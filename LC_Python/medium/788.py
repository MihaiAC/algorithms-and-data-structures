from functools import cache


@cache
def calcAns(n: int) -> int:
    if n == 1:
        return 0

    ans = calcAns(n - 1)
    curr = 0
    for digit in str(n):
        if digit in "347":
            curr = -1
            break
        elif digit in "2569":
            curr = 1
    return ans if curr <= 0 else ans + 1


class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Must not contain: 3, 4, 7.
        # Must contain one of: 2, 5, 6, 9.
        # Neutral: 0, 1, 8.
        return calcAns(n)


sol = Solution()
print(sol.rotatedDigits(10))
print(sol.rotatedDigits(1))
print(sol.rotatedDigits(2))
