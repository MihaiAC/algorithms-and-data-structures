from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        N = len(words)

        for count in range(N):
            if (
                words[(startIndex + count) % N] == target
                or words[(startIndex - count) % N] == target
            ):
                return count

        return -1


sol = Solution()
print(sol.closestTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1))
print(sol.closestTarget(["a", "b", "leetcode"], "leetcode", 0))
print(sol.closestTarget(["i", "eat", "leetcode"], "ate", 0))
