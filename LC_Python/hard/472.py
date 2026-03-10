from typing import List

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.next_letters = dict()
        self.words_so_far = set()
    
    def add_word(self, word: str):
        self.words_so_far.add(word)

        curr_node = self
        
        for letter in word:
            if letter in curr_node.next_letters:
                curr_node = curr_node.next_letters[letter]
            else:
                curr_node.next_letters[letter] = TrieNode()
                curr_node = curr_node.next_letters[letter]
        
        curr_node.isEnd = True
    
    def find_word(self, word: str) -> bool:
        if word in self.words_so_far:
            return True
        
        curr_node = self
        for ii in range(len(word)):
            if curr_node.isEnd and self.find_word(word[ii:]):
                self.words_so_far.add(word)
                return True
            elif word[ii] in curr_node.next_letters:
                curr_node = curr_node.next_letters[word[ii]]
            else:
                return False
        
        if curr_node.isEnd:
            self.words_so_far.add(word)
            return True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))

        trie = TrieNode()
        concatenated_words = []
        for word in words:
            if word in trie.words_so_far:
                continue
            else: 
                if trie.find_word(word):
                    concatenated_words.append(word)
                trie.add_word(word)
        
        return concatenated_words



if __name__ == '__main__':
    sol = Solution()
    words = ["cat","dog","catdog"]
    print(sol.findAllConcatenatedWordsInADict(words))