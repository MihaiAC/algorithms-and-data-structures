from typing import List

class Solution:
    
    def calculateNrNodesEachSubtreeAndDistancesFromRoot(self, root:int, parent_node: int, dist_from_root: int) -> int:
        nr_subtree_nodes = 0
        self.dist_from_root[root] = dist_from_root
        for neighbor in self.neighbors[root]:
            if neighbor == parent_node:
                continue
            else:
                nr_subtree_nodes += self.calculateNrNodesEachSubtreeAndDistancesFromRoot(neighbor, root, dist_from_root+1)
        
        self.nr_nodes_subtree[root] = nr_subtree_nodes
        return nr_subtree_nodes+1
    
    def calculate_answer(self, root:int, parent_node: int):
        if root == 0:
            self.answer[0] = self.sum_distances_from_root
        else:
            self.answer[root] = self.answer[parent_node] - 2*self.nr_nodes_subtree[root] + self.n - 2
        
        for neighbor in self.neighbors[root]:
            if neighbor == parent_node:
                continue
            else:
                self.calculate_answer(neighbor, root)


    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.neighbors = dict()
        self.nr_nodes_subtree = dict()
        self.dist_from_root = [0]*n
        self.answer = [0]*n
        self.n = n

        for v1, v2 in edges:
            if v1 not in self.neighbors:
                self.neighbors[v1] = set()
            self.neighbors[v1].add(v2)
            
            if v2 not in self.neighbors:
                self.neighbors[v2] = set()
            self.neighbors[v2].add(v1)
        
        self.calculateNrNodesEachSubtreeAndDistancesFromRoot(0, -1, 0)
        self.sum_distances_from_root = 0
        for dist in self.dist_from_root:
            self.sum_distances_from_root += dist
        
        self.calculate_answer(0, -1)
        return self.answer


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    print(sol.sumOfDistancesInTree(n, edges))