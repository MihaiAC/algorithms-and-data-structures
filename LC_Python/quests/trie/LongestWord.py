from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_so_far = {""}
        words.sort(key=lambda x: (len(x), x))

        max_len = 0
        ans = ""

        for word in words:
            if len(word) > max_len and word[:-1] in words_so_far:
                max_len = len(word)
                ans = word

            if word[:-1] in words_so_far:
                words_so_far.add(word)

        return ans


sol = Solution()
print(sol.longestWord(["w", "wo", "wor", "worl", "world"]))
print(sol.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(sol.longestWord(["bc"]))
