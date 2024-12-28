from typing import List

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        N = len(temps)

        if N == 1:
            return [0]
        
        deltas = [0] * N
        for ii in range(N-2, -1, -1):
            jj = ii+1
            dist = 1
            while True:
                if temps[ii] < temps[jj]:
                    deltas[ii] = dist
                    break
                else:
                    if jj >= N-1 or deltas[jj] == 0:
                        break
                dist += deltas[jj]
                jj += deltas[jj]
                
        
        return deltas

        

if __name__ == '__main__':
    sol = Solution()
    temperatures = [30,60,90]
    print(sol.dailyTemperatures(temperatures))