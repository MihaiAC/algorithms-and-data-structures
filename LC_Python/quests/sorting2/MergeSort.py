from typing import List


def mergeSort(nums: List[int], left: int, right: int):
    if left == right:
        return

    mid = (left + right) // 2
    mergeSort(nums, left, mid)
    mergeSort(nums, mid + 1, right)

    sorted_segment = []
    ii, jj = left, mid + 1

    while ii <= mid and jj <= right:
        if nums[ii] < nums[jj]:
            sorted_segment.append(nums[ii])
            ii += 1
        else:
            sorted_segment.append(nums[jj])
            jj += 1

    while ii <= mid:
        sorted_segment.append(nums[ii])
        ii += 1

    while jj <= right:
        sorted_segment.append(nums[jj])
        jj += 1

    nums[left : (right + 1)] = sorted_segment
    print(f"{left} {right} {sorted_segment}")


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mergeSort(nums, 0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    sol = Solution()
    sol.sortArray([5, 1, 1, 2, 0, 0])
