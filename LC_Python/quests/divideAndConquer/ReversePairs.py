from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0

        def mergeSort(left: int, right: int):
            nonlocal ans

            if left == right:
                return

            mid = (left + right) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)

            ii, jj = left, mid + 1
            while ii <= mid and jj <= right:
                if nums[ii] > 2 * nums[jj]:
                    ans += mid - ii + 1
                    jj += 1
                else:
                    ii += 1

            ii, jj = left, mid + 1
            merged = []
            while ii <= mid and jj <= right:
                if nums[ii] < nums[jj]:
                    merged.append(nums[ii])
                    ii += 1
                else:
                    merged.append(nums[jj])
                    jj += 1

            while ii <= mid:
                merged.append(nums[ii])
                ii += 1

            while jj <= right:
                merged.append(nums[jj])
                jj += 1

            nums[left : right + 1] = merged

        mergeSort(0, len(nums) - 1)
        return ans


if __name__ == "__main__":
    sol = Solution()

    s1 = sol.reversePairs([1, 3, 2, 3, 1])
    assert s1 == 2, f"Expected 2, got {s1} instead"

    s2 = sol.reversePairs([2, 4, 3, 5, 1])
    assert s2 == 3, f"Expected 3, got {s2} instead"
