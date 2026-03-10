from typing import List
from sortedcontainers import SortedList


class Window:
    def __init__(self, k: int):
        self.k = k
        self.curr = SortedList()
        self.reserve = SortedList()
        self.currSum = 0

    # self.curr should always have k elements if possible
    def balance(self):
        while len(self.curr) < self.k and len(self.reserve) > 0:
            reserveMin = self.reserve[0]
            self.curr.add(reserveMin)
            self.reserve.remove(reserveMin)
            self.currSum += reserveMin

        while len(self.curr) > self.k:
            currMax = self.curr[-1]
            self.reserve.add(currMax)
            self.curr.remove(currMax)
            self.currSum -= reserveMin

    # Add num to the current window.
    def add(self, num: int):
        if len(self.reserve) > 0 and num >= self.reserve[0]:
            self.reserve.add(num)
        else:
            self.curr.add(num)
            self.currSum += num
        self.balance()

    # Delete num from the current window.
    def delete(self, num: int):
        if num in self.curr:
            self.curr.remove(num)
            self.currSum -= num
        elif num in self.reserve:
            self.reserve.remove(num)
        self.balance()


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        N = len(nums)
        window = Window(k - 2)

        for ii in range(1, k - 1):
            window.add(nums[ii])

        ans = window.currSum + nums[k - 1]

        for ii in range(k, N):
            jj = ii - dist - 1

            if jj > 0:
                window.delete(nums[jj])

            window.add(nums[ii - 1])
            ans = min(ans, window.currSum + nums[ii])

        return ans + nums[0]


if __name__ == "__main__":
    sol = Solution()
    cost = sol.minimumCost([10, 8, 18, 9], 3, 1)
    print(cost)
