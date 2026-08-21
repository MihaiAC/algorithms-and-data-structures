from typing import List
from itertools import combinations
from math import lcm
from bisect import bisect_left


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()

        if coins[0] == 1:
            return k

        no_dups = [coins[0]]
        for coin in coins[1:]:
            if all([coin % x != 0 for x in no_dups]):
                no_dups.append(coin)
        coins = no_dups

        N = len(coins)

        def count_gt_k(mid: int):
            """
            Returns true if the number of multiples <= mid
            is greater than k.
            """
            count = 0
            for take_k in range(1, N + 1):
                for coin_combination in combinations(coins, take_k):
                    count += mid // lcm(*coin_combination) * (-1) ** (take_k + 1)
            return count >= k

        return bisect_left(range(k * min(coins) + 1), True, lo=1, key=count_gt_k)


sol = Solution()
print(sol.findKthSmallest([3, 6, 9], 3))
print(sol.findKthSmallest([5, 2], 7))
