from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        s = list(s)
        N = len(s)
        segments = SortedList()
        lengths = SortedList()

        def add(left: int, right: int) -> None:
            segments.add((left, right))
            lengths.add(right - left + 1)

        def pop(idx: int) -> tuple:
            left, right = segments.pop(idx)
            lengths.remove(right - left + 1)
            return left, right

        def find(pos: int) -> int:
            return segments.bisect_right((pos, N)) - 1

        left = 0
        for right in range(N):
            if s[left] != s[right]:
                add(left, right - 1)
                left = right
        add(left, N - 1)

        ans = []

        for pos, ch in zip(queryIndices, queryCharacters):
            if s[pos] == ch:
                ans.append(lengths[-1])
                continue

            # rip pos out of its segment
            left, right = pop(find(pos))
            s[pos] = ch

            # new segment, to be extended
            new_left, new_right = pos, pos

            # either split the segment the char is a part of,
            # or complete a neighbouring one

            # check left, set new_left
            if left < pos:
                add(left, pos - 1)
            elif pos > 0 and s[pos - 1] == ch:
                new_left = pop(find(pos - 1))[0]

            # check right, set new_right
            if pos < right:
                add(pos + 1, right)
            elif pos + 1 < N and s[pos + 1] == ch:
                new_right = pop(find(pos + 1))[1]

            add(new_left, new_right)
            ans.append(lengths[-1])

        return ans


sol = Solution()
print(sol.longestRepeating("babacc", "bcb", [1, 3, 3]))
print(sol.longestRepeating("abyzz", "aa", [2, 1]))
