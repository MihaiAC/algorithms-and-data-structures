from collections import Counter

class Solution:
    def calculate_similarity(self, input_file: str) -> int:
        c1, c2 = Counter(), Counter()
        with open(input_file) as file:
            for line in file:
                numbers = line.split("   ")
                c1[int(numbers[0])] += 1
                c2[int(numbers[1])] += 1
        
        similarity = 0
        for N in c1:
            similarity += N * c1[N] * c2[N]
        
        return similarity

if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate_similarity('test'))