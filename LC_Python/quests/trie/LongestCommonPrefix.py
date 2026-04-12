from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        min_len = min([len(x) for x in strs])

        left, right = 0, min_len
        while left < right:
            mid = (left + right + 1) // 2
            common = strs[0][:mid]
            if all([s[:mid] == common for s in strs[1:]]):
                left = mid
            else:
                right = mid - 1

        return strs[0][:left]


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
