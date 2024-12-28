from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_losses = set()
        one_loss = set()
        more_than_one_loss = set()
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in one_loss and winner not in more_than_one_loss:
                zero_losses.add(winner)
            if loser in zero_losses:
                zero_losses.remove(loser)
            if loser not in more_than_one_loss:
                if loser in one_loss:
                    one_loss.remove(loser)
                    more_than_one_loss.add(loser)
                else:
                    one_loss.add(loser)
        
        zero_losses_list = list(zero_losses)
        one_loss_list = list(one_loss)

        zero_losses_list.sort()
        one_loss_list.sort()

        return [zero_losses_list, one_loss_list]


if __name__ == '__main__':
    sol = Solution()
    matches = [[2,3],[1,3],[5,4],[6,4]]
    print(sol.findWinners(matches))