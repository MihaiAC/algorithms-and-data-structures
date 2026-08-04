from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m, M = 101, 0
        elems = set()

        for num in nums:
            m = min(num, m)
            M = max(num, M)
            elems.add(num)

        ans = []
        for num in range(m + 1, M):
            if num not in elems:
                ans.append(num)

        return ans


sol = Solution()
print(sol.findMissingElements([5, 1]))
