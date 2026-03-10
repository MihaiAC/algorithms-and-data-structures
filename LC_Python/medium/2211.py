class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        left, right = 0, len(directions) - 1

        while left <= right and directions[left] == "L":
            left += 1

        while left <= right and directions[right] == "R":
            right -= 1

        for idx in range(left, right + 1):
            if directions[idx] != "S":
                ans += 1

        return ans
