class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = [0] * 26
        for letter in word:
            counter[ord(letter) - 97] += 1

        counter.sort()

        curr_presses = 1
        curr_button = 0
        ans = 0
        for freq in counter[::-1]:
            if freq == 0:
                break

            if curr_button == 8:
                curr_button = 0
                curr_presses += 1

            ans += curr_presses * freq
            curr_button += 1

        return ans


sol = Solution()
print(sol.minimumPushes("abcde"))
print(sol.minimumPushes("xycdefghij"))
