class Solution:
    def sortString(self, s: str) -> str:
        sorted_str = []
        letters = dict()
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        total = len(s)
        sorted_letters = list(letters.keys())
        sorted_letters.sort()

        while True:
            for letter in sorted_letters:
                if letter in letters:
                    sorted_str.append(letter)
                    if letters[letter] == 1:
                        del letters[letter]
                    else:
                        letters[letter] -= 1
                    total -= 1
                    if total == 0:
                        return ''.join(sorted_str)
            
            for ii in range(len(sorted_letters)-1, -1, -1):
                letter = sorted_letters[ii]
                if letter in letters:
                    sorted_str.append(letter)
                    if letters[letter] == 1:
                        del letters[letter]
                    else:
                        letters[letter] -= 1
                    total -= 1
                    if total == 0:
                        return ''.join(sorted_str)


if __name__ == '__main__':
    sol = Solution()
    s = "aaaabbbbcccc"
    print(sol.sortString(s))