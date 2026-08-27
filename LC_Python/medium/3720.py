from collections import Counter
from typing import Dict


def find_smallest_letter_bigger_than(counts: Dict[str, int], target_letter: str) -> str:
    min_letter = ""
    for letter in counts:
        if counts[letter] > 0 and letter > target_letter:
            if min_letter == "":
                min_letter = letter
            else:
                min_letter = min(min_letter, letter)
    return min_letter


def min_string(counts: Dict[str, int]) -> str:
    res = []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if counts[letter] > 0:
            res.append(letter * counts[letter])
    return "".join(res)


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        N = len(target)
        counts = Counter(s)
        curr_idx = 0

        # Match phase.
        while curr_idx < N:
            letter = target[curr_idx]
            if counts[letter] > 0:
                counts[letter] -= 1
                curr_idx += 1
            else:
                break

        if curr_idx < N:
            min_letter = find_smallest_letter_bigger_than(counts, target[curr_idx])
            if min_letter != "":
                counts[min_letter] -= 1
                return target[:curr_idx] + min_letter + min_string(counts)

        # Backtrack until we find an available letter bigger than the current one.
        while curr_idx > 0:
            curr_idx -= 1
            counts[target[curr_idx]] += 1

            min_letter = find_smallest_letter_bigger_than(counts, target[curr_idx])
            if min_letter != "":
                counts[min_letter] -= 1
                return target[:curr_idx] + min_letter + min_string(counts)

        return ""


sol = Solution()
print(sol.lexGreaterPermutation("abc", "bba"))
print(sol.lexGreaterPermutation("leet", "code"))
print(sol.lexGreaterPermutation("baba", "bbaa"))
