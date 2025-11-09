class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        n_ops = 0
        while num1 != 0 and num2 != 0:
            num1, num2 = max(num1, num2), min(num1, num2)
            n_ops += num1 // num2
            num1 = num1 % num2
        
        return n_ops
