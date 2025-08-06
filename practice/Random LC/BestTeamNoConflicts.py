from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)

        player_stats = [(scores[ii], ages[ii]) for ii in range(N)]
        player_stats.sort() 
        
        max_score_for_age = [0] * (max(ages)+1)

        for score, age in player_stats:
            max_score_for_age[age] = score + max(max_score_for_age[0:age+1])
        
        return max(max_score_for_age)




if __name__ == '__main__':
    sol = Solution()
    scores = [1,2,3,5]
    ages = [8,9,10,1]
    print(sol.bestTeamScore(scores, ages))