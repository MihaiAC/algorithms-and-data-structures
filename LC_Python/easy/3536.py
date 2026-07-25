class Solution:
    def maxProduct(self, n: int) -> int:
        ans = 0
        max_so_far = 0

        while n > 0:
            digit = n % 10
            n = n // 10

            ans = max(ans, max_so_far * digit)
            max_so_far = max(max_so_far, digit)

        return ans


sol = Solution()
print(sol.maxProduct(31))
print(sol.maxProduct(22))
print(sol.maxProduct(124))
