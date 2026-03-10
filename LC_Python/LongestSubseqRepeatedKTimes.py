from collections import Counter, deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> int:
        ans = ""

        counter = Counter(s)
        candidates = []
        for letter in counter:
            if counter[letter] >= k:
                candidates.append(letter)
        candidates.sort(reverse=True)

        queue = deque(candidates)
        while len(queue) > 0:
            curr_candidate = queue.popleft()
            if len(curr_candidate) > len(ans):
                ans = curr_candidate

            # Really neat iterator trick.
            for letter in candidates:
                next_candidate = curr_candidate + letter
                s_iterator = iter(s)
                if all(letter in s_iterator for letter in next_candidate * k):
                    queue.append(next_candidate)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubsequenceRepeatedK("letsleetcode", 2))
