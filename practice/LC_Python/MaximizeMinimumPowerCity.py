class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)

        # Change at ii.
        count = [0]*(N+1)
        
        for ii in range(N):
            left_reach = max(0, ii-r)
            right_reach = min(N, ii+r+1)
            
            count[left_reach] += stations[ii]
            count[right_reach] -= stations[ii]
        
        def check(target_power: int) -> bool:  
            diff = count.copy()

            # Accum for curr city
            current_power = 0
            remaining = k
            
            for ii in range(N):
                current_power += diff[ii]
                
                if current_power < target_power:
                    need = target_power - current_power
    
                    if remaining < need:
                        return False
                    
                    remaining -= need
                    end_of_effect = min(N, ii + 2*r + 1)
                    diff[end_of_effect] -= need
                    
                    current_power += need
            
            return True
        
        # Binary search for maximum achievable power
        lo, hi = min(stations), sum(stations) + k
        res = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res
