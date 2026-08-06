from functools import reduce


def get_digit_product(x: int) -> int:
    return reduce(lambda x, y: x * int(y), list(str(x)), initial=1)


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for x in range(n, n + 11):
            if get_digit_product(x) % t == 0:
                return x


sol = Solution()
print(sol.smallestNumber(10, 2))
print(sol.smallestNumber(15, 3))
