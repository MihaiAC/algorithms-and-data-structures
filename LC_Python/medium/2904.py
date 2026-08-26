def init_or_min(old: str, new: str) -> str:
    if old == "":
        return new

    if len(old) < len(new):
        return old
    elif len(new) < len(old):
        return new
    return min(old, new)


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        curr_ones = 0
        left = 0

        for right in range(len(s)):
            if s[right] == "1":
                curr_ones += 1

                while (curr_ones > k or s[left] == "0") and left < right:
                    if s[left] == "1":
                        curr_ones -= 1
                    left += 1

                if curr_ones == k:
                    ans = init_or_min(ans, s[left : (right + 1)])

        return ans


sol = Solution()
print(sol.shortestBeautifulSubstring("100011001", 3))
print(sol.shortestBeautifulSubstring("1011", 2))
print(sol.shortestBeautifulSubstring("000", 1))
