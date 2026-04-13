from typing import List


def countBouquets(bloomDay: List[int], currDay: int, k: int) -> int:
    count = 0
    streak = 0

    for day in bloomDay:
        if day <= currDay:
            streak += 1
            if streak == k:
                count += 1
                streak = 0
        else:
            streak = 0

    return count


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        if n < m * k:
            return -1

        left, right = 0, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if countBouquets(bloomDay, mid, k) >= m:
                right = mid
            else:
                left = mid + 1

        return left


sol = Solution()
print(sol.minDays([1, 10, 3, 10, 2], 3, 1))
print(sol.minDays([1, 10, 3, 10, 2], 3, 2))
print(sol.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))
