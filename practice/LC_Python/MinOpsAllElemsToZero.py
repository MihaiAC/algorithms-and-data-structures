class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        n_ops = 0
        
        for num in nums:
            while len(stack) > 0 and num < stack[-1]:
                stack.pop()
                n_ops += 1
            
            if num != 0 and (len(stack) == 0 or num > stack[-1]):
                stack.append(num)
        
        n_ops += len(stack)
        return n_ops

if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations([2, 1, 2, 1, 3]))