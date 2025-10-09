from typing import List

class Solution:
    def minTime(self, wizard_skill: List[int], mana_values: List[int]) -> int:
        N_wizards = len(wizard_skill)
        earliest_avail = [0]*N_wizards
        for mana in mana_values:
            earliest_avail[0] += wizard_skill[0] * mana
            for idx in range(1, N_wizards):
                earliest_avail[idx] = max(earliest_avail[idx], earliest_avail[idx-1]) + wizard_skill[idx]*mana

            # Backpass.
            for idx in range(N_wizards-2, -1, -1):
                earliest_avail[idx] = earliest_avail[idx+1]-mana*wizard_skill[idx+1]
        return earliest_avail[-1]
