class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Must not contain: 3, 4, 7.
        # Must contain one of: 2, 5, 6, 9.
        # Neutral: 0, 1, 8.
        ans = 0
        for num in range(1, n + 1):
            contains_bad = False
            contains_good = False
            for digit in str(num):
                if digit in "347":
                    contains_bad = True
                    break
                elif digit in "2569":
                    contains_good = True
            if not contains_bad and contains_good:
                ans += 1
        return ans


sol = Solution()
print(sol.rotatedDigits(10))
print(sol.rotatedDigits(1))
print(sol.rotatedDigits(2))
