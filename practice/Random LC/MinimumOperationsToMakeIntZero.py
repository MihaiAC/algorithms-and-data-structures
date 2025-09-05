class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for ans in range(1, 61):
            num1 -= num2
            
            if num1 < ans:
                return -1
            
            if ans >= num1.bit_count():
                return ans
        
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.makeTheIntegerZero(3, -2))