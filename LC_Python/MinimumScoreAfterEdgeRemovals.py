from typing import Dict, List, Tuple, Set
from collections import defaultdict, deque
from functools import reduce

def build_tree(neighbors: Dict[int, List[int]]) -> Tuple[Dict[int, List[int]], Dict[int, int]]:
    children = defaultdict(list)
    parent = defaultdict(int)
    visited = set()
    queue = deque()
        
    queue.appendleft(0)
    visited.add(0)

    while len(queue) > 0:
        node = queue.pop()
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.appendleft(neighbor)
                children[node].append(neighbor)
                parent[neighbor] = node
    
    return children, parent

def precompute_with_dfs(
    nums: List[int], 
    children: Dict[int, List[int]]
) -> Tuple[Dict[int, int], Dict[int, Set[int]]]:
    
    subtree_xor = {}
    descendants = defaultdict(set)

    def dfs(node: int) -> Tuple[int, Set[int]]:
        current_xor = nums[node]
        current_descendants = set()

        for child in children[node]:
            child_xor, child_descendants = dfs(child)
            
            current_xor ^= child_xor
            current_descendants.update(child_descendants)
            current_descendants.add(child)

        # Store the final computed values for this node.
        subtree_xor[node] = current_xor
        descendants[node] = current_descendants
        
        return current_xor, current_descendants
    
    dfs(0)
    return subtree_xor, descendants


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        # Build tree.
        children, parent = build_tree(neighbors)

        # Calculate total XOR.
        total_XOR = reduce(lambda x, y: x^y, nums)
        
        # Pre-compute all necessary information in a single pass.
        subtree_xor, descendants = precompute_with_dfs(nums, children)
        
        ans = float('inf')
        
        # Nodes with an edge coming "into" them.
        edge_nodes = list(range(1, len(nums)))

        # Iterate through all unique pairs of edges to cut.
        for ii in range(len(edge_nodes)-1):
            for jj in range(ii+1, len(edge_nodes)):
                # c1 and c2 are the child nodes of the two edges we are cutting.
                c1 = edge_nodes[ii]
                c2 = edge_nodes[jj]

                # Retrieve the pre-calculated XOR sums for the subtrees of c1 and c2.
                xor1 = subtree_xor[c1]
                xor2 = subtree_xor[c2]
                
                # Subtree of c1 contains the subtree of c2.
                if c2 in descendants[c1]:
                    a = xor2
                    b = xor1 ^ xor2
                    c = total_XOR ^ xor1
                # Subtree of c2 contains the subtree of c1.
                elif c1 in descendants[c2]:
                    a = xor1
                    b = xor2 ^ xor1
                    c = total_XOR ^ xor2
                # Disjoint subtrees.
                else:
                    a = xor1
                    b = xor2
                    c = total_XOR ^ xor1 ^ xor2
                
                score = max(a, b, c) - min(a, b, c)
                ans = min(ans, score)

        return ans
    
if __name__ == '__main__':
    sol = Solution()
    nums = [1,5,5,4,11]
    edges = [[0,1],[1,2],[1,3],[3,4]]

    print(sol.minimumScore(nums, edges))