class Solution:
    def sumGame(self, num: str) -> bool:
        N = len(num)
        digit_sums = [0, 0]
        q_marks = [0, 0]

        for idx, char in enumerate(num):
            half_idx = 1 if idx >= (N // 2) else 0
            if char == "?":
                q_marks[half_idx] += 1
            else:
                digit_sums[half_idx] += int(char)

        return (
            sum(q_marks) % 2 == 1
            or digit_sums[0] - digit_sums[1] != (q_marks[1] - q_marks[0]) * 9 // 2
        )


sol = Solution()
print(sol.sumGame("5023"))
print(sol.sumGame("25??"))
print(sol.sumGame("?3295???"))
