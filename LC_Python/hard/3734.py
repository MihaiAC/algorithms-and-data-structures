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
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        N = len(target)
        counts = Counter(s)

        mid = ""
        odd_count = 0
        for letter in counts:
            if counts[letter] % 2 == 1:
                odd_count += 1
                mid = letter
            counts[letter] //= 2

        if odd_count > 1:
            return ""

        half = N // 2
        curr_idx = 0

        # Match phase, bounded to the first half.
        while curr_idx < half:
            letter = target[curr_idx]
            if counts[letter] > 0:
                counts[letter] -= 1
                curr_idx += 1
            else:
                break

        if curr_idx == half:
            first_half = target[:half]
            candidate = first_half + mid + first_half[::-1]
            if candidate > target:
                return candidate
        elif curr_idx < half:
            min_letter = find_smallest_letter_bigger_than(counts, target[curr_idx])
            if min_letter != "":
                counts[min_letter] -= 1
                first_half = target[:curr_idx] + min_letter + min_string(counts)
                return first_half + mid + first_half[::-1]

        # Backtrack until we find an available letter bigger than the current one.
        while curr_idx > 0:
            curr_idx -= 1
            counts[target[curr_idx]] += 1

            min_letter = find_smallest_letter_bigger_than(counts, target[curr_idx])
            if min_letter != "":
                counts[min_letter] -= 1
                first_half = target[:curr_idx] + min_letter + min_string(counts)
                return first_half + mid + first_half[::-1]

        return ""


sol = Solution()
print(sol.lexPalindromicPermutation("baba", "abba"))
print(sol.lexPalindromicPermutation("baba", "bbaa"))
print(sol.lexPalindromicPermutation("abc", "abb"))
print(sol.lexPalindromicPermutation("aac", "abb"))
