from time import time
from random import randint

from numpy import argsort

class Solution:
    IDX_TO_LETTER = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: 'A', 27: 'B', 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G', 33: 'H', 34: 'I', 35: 'J', 36: 'K', 37: 'L', 38: 'M', 39: 'N', 40: 'O', 41: 'P', 42: 'Q', 43: 'R', 44: 'S', 45: 'T', 46: 'U', 47: 'V', 48: 'W', 49: 'X', 50: 'Y', 51: 'Z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9'}
    LETTER_TO_IDX = {'0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, 'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'H': 33, 'I': 34, 'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42, 'R': 43, 'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51}

    def frequencySort(self, s: str) -> str:
        letterToFreq = [0] * 62

        for letter in s:
            letterToFreq[Solution.LETTER_TO_IDX[letter]] += 1
        
        sorted_indices = argsort(letterToFreq)

        sorted_string_as_list = []
    
        for ii in range(len(sorted_indices)-1, -1, -1):
            true_index = sorted_indices[ii]
            true_letter = Solution.IDX_TO_LETTER[true_index]
            for _ in range(letterToFreq[true_index]):
                sorted_string_as_list.append(true_letter)
        
        return ''.join(sorted_string_as_list)

if __name__ == '__main__':
    sol = Solution()

    letters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s_letters = []

    for _ in range(500000):
        s_letters.append(letters[randint(0, len(letters)-1)])

    s = ''.join(s_letters)

    t_start = time()
    sol.frequencySort(s)
    t_end = time()

    print(t_end-t_start)