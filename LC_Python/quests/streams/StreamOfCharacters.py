from typing import List


class TrieNode:
    def __init__(self):
        self.next = dict()
        self.is_end = False

    def add_word(self, word: str):
        curr = self

        for letter in word:
            if letter not in curr.next:
                curr.next[letter] = TrieNode()
            curr = curr.next[letter]

        curr.is_end = True


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.root.add_word(word)

        self.curr_nodes = []

    def query(self, letter: str) -> bool:
        next_nodes = []

        found = False
        for node in self.curr_nodes:
            if letter in node.next:
                next_nodes.append(node.next[letter])
                if next_nodes[-1].is_end:
                    found = True

        if letter in self.root.next:
            next_nodes.append(self.root.next[letter])
            if next_nodes[-1].is_end:
                found = True

        self.curr_nodes = next_nodes
        return found
