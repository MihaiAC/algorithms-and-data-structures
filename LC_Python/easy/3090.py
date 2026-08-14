class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        ans, left_idx = 0, 0

        for right_idx, letter in enumerate(s):
            chr_idx = ord(letter) - 97
            count[chr_idx] += 1

            while count[chr_idx] > 2:
                count[ord(s[left_idx]) - 97] -= 1
                left_idx += 1

            ans = max(ans, right_idx - left_idx + 1)

        return ans


sol = Solution()
print(sol.maximumLengthSubstring("bcbbbcba"))
print(sol.maximumLengthSubstring("aaaa"))
