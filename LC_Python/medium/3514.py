from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        singles = set()
        pairs = set()
        triplets = set()

        for num in nums:
            singles.add(num)

            for single in singles:
                pairs.add(num ^ single)

            for pair in pairs:
                triplets.add(num ^ pair)

        return len(triplets)


sol = Solution()
print(sol.uniqueXorTriplets([1, 3]))
print(sol.uniqueXorTriplets([6, 7, 8, 9]))
