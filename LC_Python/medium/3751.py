def getWaviness(num: int) -> int:
    str_num = str(num)
    if len(str_num) < 3:
        return 0

    trend = 0
    if str_num[1] > str_num[0]:
        trend = 1

    if str_num[1] < str_num[0]:
        trend = -1

    waviness = 0
    for idx in range(2, len(str_num)):
        digit = str_num[idx]
        if digit > str_num[idx - 1]:
            if trend == -1:
                waviness += 1
            trend = 1
        elif digit < str_num[idx - 1]:
            if trend == 1:
                waviness += 1
            trend = -1
        else:
            trend = 0

    return waviness


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for num in range(num1, num2 + 1):
            waviness += getWaviness(num)
        return waviness


sol = Solution()
print(sol.totalWaviness(120, 130))
print(sol.totalWaviness(198, 202))
print(sol.totalWaviness(4848, 4848))
