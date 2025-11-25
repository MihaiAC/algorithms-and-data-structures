class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        if k == 1:
            return 1

        num = 1
        ans = 1
        while ans < k and num != 0:
            ans += 1
            num = (num * 10 + 1) % k

        if num == 0:
            return ans
        return -1
