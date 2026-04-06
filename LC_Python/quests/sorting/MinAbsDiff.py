from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        minDiff = arr[-1] - arr[0]

        for idx in range(len(arr) - 1):
            currDiff = arr[idx + 1] - arr[idx]
            if currDiff < minDiff:
                ans = [[arr[idx], arr[idx + 1]]]
                minDiff = currDiff
            elif currDiff == minDiff:
                ans.append([arr[idx], arr[idx + 1]])

        return ans
