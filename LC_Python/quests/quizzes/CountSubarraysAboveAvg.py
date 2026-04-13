from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0

        curr_sum = sum(arr[:k])
        if curr_sum // k >= threshold:
            count += 1

        for idx in range(k, len(arr)):
            curr_sum -= arr[idx - k]
            curr_sum += arr[idx]

            if curr_sum // k >= threshold:
                count += 1

        return count


sol = Solution()
print(sol.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
print(sol.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
