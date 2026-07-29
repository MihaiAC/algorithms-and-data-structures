from math import comb


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        N = len(s)
        n = N // 2

        counter = [0] * 26
        for letter in s[:n]:
            counter[ord(letter) - 97] += 1

        def count_permutations(slots: int) -> int:
            ways = 1
            for idx in range(26):
                if counter[idx] == 0:
                    continue
                ways *= comb(slots, counter[idx])
                slots -= counter[idx]

                if ways > k:
                    break

            return ways

        curr_count = 0
        half = []

        for pos in range(n):
            placed = False

            for letter_idx in range(26):
                if counter[letter_idx] == 0:
                    continue

                counter[letter_idx] -= 1
                ways = count_permutations(n - pos - 1)

                if curr_count + ways >= k:
                    half.append(chr(letter_idx + 97))
                    placed = True
                    break

                counter[letter_idx] += 1
                curr_count += ways

            if not placed:
                break

        if len(half) < n:
            return ""

        left = "".join(half)
        mid = s[n] if N % 2 else ""

        return left + mid + left[::-1]


sol = Solution()
print(sol.smallestPalindrome("abba", 2))
print(sol.smallestPalindrome("aa", 2))
print(sol.smallestPalindrome("bacab", 1))
print(sol.smallestPalindrome("cypspyc", 11))
