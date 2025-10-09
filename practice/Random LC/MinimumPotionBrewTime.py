from typing import List

class Solution:
    def minTime(self, wizard_skill: List[int], mana_values: List[int]) -> int:
        N_wizards = len(wizard_skill)
        N_potions = len(mana_values)

        accum = [0]
        for skill in wizard_skill:
            accum.append(skill + accum[-1])
        
        time = 0
        for mana_idx in range(1, N_potions):
            max_diff = 0
            for wizard_idx in range(N_wizards):
                max_diff = max(max_diff, accum[wizard_idx+1] * mana_values[mana_idx-1] - accum[wizard_idx] * mana_values[mana_idx])
            time += max_diff
        
        return time + accum[-1] * mana_values[-1]
