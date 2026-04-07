from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        left, right = 0, N - 1
        while left < right:
            mid = (left + right) // 2

            # Check if mid is the peak.
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid] > arr[mid + 1]:
                right = mid - 1

        return left


if __name__ == "__main__":
    sol = Solution()
    assert sol.peakIndexInMountainArray([0, 1, 0]) == 1
    assert sol.peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert sol.peakIndexInMountainArray([0, 10, 5, 2]) == 1
    assert sol.peakIndexInMountainArray([18, 29, 38, 59, 98, 100, 99, 98, 90]) == 5
