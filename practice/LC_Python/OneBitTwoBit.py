from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        N = len(bits)
        while idx < N:   
            if bits[idx] == 0:
                if idx == N-1:
                    return True
                idx += 1
            else:
                idx += 2

        return False
