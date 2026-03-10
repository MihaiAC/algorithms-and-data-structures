from typing import Dict, Set, Tuple

class Solution:
    @staticmethod
    def getLetterFrequencyAndSet(word: str) -> Tuple[Dict[str, int], Set[str]]:
        letter_set = set()
        letter_freq = dict()

        for letter in word:
            letter_set.add(letter)

            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
        
        return (letter_freq, letter_set)

    @staticmethod
    def getFrequencyOfFrequencies(letter_freqs: Dict[str, int]) -> Dict[int, int]:
        freq_freqs = dict()

        for freq in letter_freqs.values():
            if freq in freq_freqs:
                freq_freqs[freq] += 1
            else:
                freq_freqs[freq] = 1
        
        return freq_freqs

    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_freqs, word1_set = Solution.getLetterFrequencyAndSet(word1)
        word2_freqs, word2_set = Solution.getLetterFrequencyAndSet(word2)

        word_set_union = word1_set.union(word2_set)
        if len(word_set_union) > len(word1_set):
            return False
        
        word2_inverse_freq = Solution.getFrequencyOfFrequencies(word2_freqs)

        for letter in word1_freqs:
            letter_freq = word1_freqs[letter]
            if letter_freq not in word2_inverse_freq:
                return False
            else:
                freq_freq = word2_inverse_freq[letter_freq]
                if freq_freq == 1:
                    del word2_inverse_freq[letter_freq]
                else:
                    word2_inverse_freq[letter_freq] -= 1

        return True

        


if __name__ == '__main__':
    sol = Solution()
    word1 = "a"
    word2 = "aa"
    print(sol.closeStrings(word1, word2))