from typing import List


class TrieNode:
    def __init__(self):
        self.next = dict()
        self.is_end = False

    def add_string(self, string: str):
        curr_node = self
        for letter in string:
            if letter not in curr_node.next:
                curr_node.next[letter] = TrieNode()
            curr_node = curr_node.next[letter]
        curr_node.is_end = True

    def calc_max(self, string: str) -> int:
        ans = []
        curr_node = self
        for letter in string:
            inv_letter = "0" if letter == "1" else "1"
            if inv_letter in curr_node.next:
                curr_node = curr_node.next[inv_letter]
                ans.append("1")
            else:
                curr_node = curr_node.next[letter]
                ans.append("0")
        return int("".join(ans), 2)


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = TrieNode()
        for num in nums:
            trie.add_string(format(num, "032b"))

        ans = 0
        for num in nums:
            ans = max(ans, trie.calc_max(format(num, "032b")))

        return ans


sol = Solution()
print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))
print(sol.findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))
