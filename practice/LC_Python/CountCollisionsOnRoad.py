class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        stack = []

        for direction in directions:
            if direction == "L":
                if len(stack) == 0:
                    continue
                elif stack[-1] == "R":
                    ans += 2
                    stack.pop()
                    while stack and stack[-1] == "R":
                        stack.pop()
                        ans += 1
                    if not stack:
                        stack.append("S")
                else:
                    ans += 1
            elif direction == "S":
                while stack and stack[-1] == "R":
                    stack.pop()
                    ans += 1
                stack.append("S")
            else:
                stack.append("R")

        return ans
