from typing import List, Dict

from collections import deque

class Solution:
    @staticmethod
    def addToDict(key: int, value:int, dictionary: Dict):
        if key in dictionary:
            dictionary[key].add(value)
        else:
            dictionary[key] = set()
            dictionary[key].add(value)

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        neighbors = dict()
        for v1, v2 in dislikes:
            Solution.addToDict(v1, v2, neighbors)
            Solution.addToDict(v2, v1, neighbors)
        
        group = dict()
        for node in range(1, n+1):
            if node in group:
                continue
            group[node] = 0
            queue = deque()
            queue.appendleft(node)
            while len(queue) > 0:
                curr_node = queue.pop()
                opposite_group = 1 - group[curr_node]

                # If the node has no neighbors, assign it to a group at random.
                if curr_node not in neighbors:
                    continue

                for neighbor in neighbors[curr_node]:
                    if neighbor in group:
                        if group[neighbor] != opposite_group:
                            return False
                        else:
                            continue
                    else:
                        group[neighbor] = opposite_group
                        queue.appendleft(neighbor)
        
        return True
        



if __name__ == '__main__':
    sol = Solution()
    n = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    print(sol.possibleBipartition(n, dislikes))