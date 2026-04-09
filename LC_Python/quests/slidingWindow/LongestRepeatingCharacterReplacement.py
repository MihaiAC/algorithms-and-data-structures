from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        if k >= N:
            return N

        left = 0
        ans = 0
        counter = defaultdict(int)

        for right in range(N):
            counter[s[right]] += 1
            highest_freq = max(counter.values())

            while left < right and right - left + 1 - highest_freq > k:
                counter[s[left]] -= 1
                left += 1

                # I mean, technically it's O(1)
                highest_freq = max(counter.values())

            ans = max(ans, right - left + 1)

        return ans


sol = Solution()
assert sol.characterReplacement("ABAB", 2) == 4
assert sol.characterReplacement("AABABBA", 1) == 4
