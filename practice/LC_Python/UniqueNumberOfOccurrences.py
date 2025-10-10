from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        elem_count = dict()

        for elem in arr:
            if elem in elem_count:
                elem_count[elem] += 1
            else:
                elem_count[elem] = 1
            
        return len(set(elem_count.values())) == len(elem_count.values())


if __name__ == '__main__':
    sol = Solution()
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(sol.uniqueOccurrences(arr))