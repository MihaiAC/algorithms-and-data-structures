from typing import Tuple

class Solution:
    def __init__(self, input_file):
        self.sequence = []
        with open(input_file) as f:
            for line in f:
                self.sequence = list(line)
        
        self.BANNED_LETTERS = ['i', 'o', 'l']

    
    def next_letter(self, letter: str) -> Tuple[str, bool]:
        if letter == 'z':
            return ('a', True)
        return (chr(ord(letter)+1), False)

    def increment_sequence(self):
        for idx in range(len(self.sequence)-1, -1, -1):
            new_letter, carry = self.next_letter(self.sequence[idx])
            self.sequence[idx] = new_letter
            if not carry:
                break

    def validate_seq(self) -> bool:
        # Check if the sequence contains 'i', 'o', or 'l'.
        for letter in self.BANNED_LETTERS:
            if letter in self.sequence:
                return False
        
        # Check if the sequence contains three consecutive letters.
        contains_consec = False
        for idx in range(len(self.sequence)-2):
            nl1, c1 = self.next_letter(self.sequence[idx])
            nl2, c2 = self.next_letter(nl1)
            if not c1 and not c2 and nl1 == self.sequence[idx+1] and nl2 == self.sequence[idx+2]:
                contains_consec = True
                break
        
        if not contains_consec:
            return False
        
        # Check if the sequence contains two different pairs of letters.
        doubles = []
        for idx in range(len(self.sequence)-1):
            if self.sequence[idx] == self.sequence[idx+1]:
                doubles.append(self.sequence[idx])
        doubles.sort()
        contains_pair = False
        for idx in range(len(doubles)-1):
            if doubles[idx] != doubles[idx+1]:
                contains_pair = True
                break
        
        if not contains_pair:
            return False
        
        return True
    
    def find_next_valid_password(self) -> str:
        self.increment_sequence()
        while not self.validate_seq():
            self.increment_sequence()
        return "".join(self.sequence)

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.find_next_valid_password())