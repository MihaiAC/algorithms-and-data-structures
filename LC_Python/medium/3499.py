class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        intervals = []

        curr_char = s[0]
        curr_count = 1

        for char in s[1:]:
            if char == curr_char:
                curr_count += 1
            else:
                intervals.append([curr_char, curr_count])
                curr_char = char
                curr_count = 1
        intervals.append([curr_char, curr_count])

        ones_count = 0
        zeros_count = 0
        for idx, (char, count) in enumerate(intervals):
            if char == "1":
                ones_count += count
                continue

            if idx + 2 < len(intervals):
                zeros_count = max(zeros_count, count + intervals[idx + 2][1])

        return zeros_count + ones_count


sol = Solution()
print(sol.maxActiveSectionsAfterTrade("01"))
print(sol.maxActiveSectionsAfterTrade("0100"))
print(sol.maxActiveSectionsAfterTrade("1000100"))
print(sol.maxActiveSectionsAfterTrade("01010"))
