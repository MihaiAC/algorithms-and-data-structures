class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs((hour % 12) * 30 - 11 * minutes / 2)
        return min(angle, 360 - angle)


sol = Solution()
print(sol.angleClock(12, 30))
print(sol.angleClock(3, 30))
print(sol.angleClock(3, 15))
print(sol.angleClock(1, 57))
