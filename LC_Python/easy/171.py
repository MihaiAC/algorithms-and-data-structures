class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        base = 1

        for idx in range(len(columnTitle) - 1, -1, -1):
            letter = columnTitle[idx]
            ans += (ord(letter) - ord("A") + 1) * base
            base *= 26

        return ans


sol = Solution()
print(sol.titleToNumber("A"))
print(sol.titleToNumber("AB"))
print(sol.titleToNumber("ZY"))
