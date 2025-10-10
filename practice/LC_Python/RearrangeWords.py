class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        words[0] = str.lower(words[0])
        words.sort(key=lambda x: len(x))
        words[0] = words[0].capitalize()
        return ' '.join(words)

if __name__ == '__main__':
    sol = Solution()
    text = "Leetcode is cool"
    print(sol.arrangeWords(text))