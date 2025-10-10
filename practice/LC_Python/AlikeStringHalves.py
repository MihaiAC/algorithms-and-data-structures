class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        nr_vowels_fh = 0
        nr_vowels_lh = 0
        vowels = set(list('aeiouAEIOU'))

        for ii in range(len(s)//2):
            if s[ii] in vowels:
                nr_vowels_fh += 1
        
        for ii in range(len(s)//2, len(s)):
            if s[ii] in vowels:
                nr_vowels_lh += 1
        
        return nr_vowels_lh == nr_vowels_fh

        

if __name__ == '__main__':
    sol = Solution()
    s = 'textbook'
    print(sol.halvesAreAlike(s))