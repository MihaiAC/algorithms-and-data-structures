from typing import List

class TrieNode:
    def __init__(self, is_end: bool=False):
        self.is_end = is_end
        self.transitions = dict()

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.add_word(word)

    def add_word(self, word: str):
        curr_node = self.root
        for letter in word:
            if letter in curr_node.transitions:
                curr_node = curr_node.transitions[letter]
            else:
                new_node = TrieNode()
                curr_node.transitions[letter] = new_node
                curr_node = new_node
        curr_node.is_end = True

    def parse_word(self, word: str) -> bool:
        curr_states = set()
        curr_states.add(self.root)
        for letter in word:
            if len(curr_states) == 0:
                return False
            
            next_states = set()
            for state in curr_states:
                if letter in state.transitions:
                    next_state = state.transitions[letter]
                    next_states.add(next_state)
                    if next_state.is_end:
                        next_states.add(self.root)
            
            curr_states = next_states
        return self.root in curr_states

class Solution:
    def __init__(self, input_file: str):
        all_input = open(input_file).read().strip().split('\n')
        self.words_to_validate = all_input[2:]
        self.trie = Trie(all_input[0].split(', '))

    def count_valid_words(self) -> int:
        n_valid = 0
        for word in self.words_to_validate:
            if self.trie.parse_word(word):
                n_valid += 1
        return n_valid


if __name__ == '__main__':
    sol = Solution('input')
    print(sol.count_valid_words())
