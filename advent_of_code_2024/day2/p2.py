from typing import List

class Solution:
    def is_increasing(self, nums: List[int]) -> bool:
        n_increasing = 0
        for idx in range(1, len(nums)):
            if nums[idx-1] < nums[idx]:
                n_increasing += 1
            elif nums[idx-1] > nums[idx]:
                n_increasing -= 1
        
        if n_increasing > 0:
            return True
        return False

    def calculate_n_safe_reports(self, input_file: str) -> int:
        n_safe_reports = 0
        within_bounds = lambda x, y: x != y and abs(x-y) <= 3
        inc_cond = lambda x, y: x < y and within_bounds(x, y)
        dec_cond = lambda x, y: x > y and within_bounds(x, y)

        with open(input_file) as f:
            for line in f:
                nums = [int(x) for x in line.split(" ")]
                
                if self.is_increasing(nums):
                    cond = inc_cond
                else:
                    cond = dec_cond
                
                n_violations = 0
                violation_indices = []

                for idx in range(len(nums)-1):
                    if not cond(nums[idx], nums[idx+1]):
                        n_violations += 1
                        violation_indices.append(idx)
                        continue
                
                # If there is a rule violation, check if we can correct it.
                if n_violations == 0:
                    n_safe_reports += 1
                elif n_violations == 1:
                    if violation_indices[0] == 0 or violation_indices[0] == len(nums)-2:
                        n_safe_reports += 1
                    else:
                        idx = violation_indices[0]
                        if cond(nums[idx-1], nums[idx+1]) or cond(nums[idx], nums[idx+2]):
                            n_safe_reports += 1
                elif n_violations == 2:
                    if violation_indices[-1] != violation_indices[0]+1:
                        continue
                    idx = violation_indices[0]
                    if cond(nums[idx], nums[idx+2]):
                        n_safe_reports += 1

        return n_safe_reports



if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate_n_safe_reports("input"))
