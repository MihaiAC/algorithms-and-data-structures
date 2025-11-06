from typing import List
from heapq import heapq
from collections import defaultdict

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = dict()

        for v in range(1, c+1):
            parent[v] = v
        
        def find_root(v: int) -> int:
            if (v == parent[v]):
                return v
            return find_root(parent[v])
        
        def union(u: int, v: int):
            a = find_root(u)
            b = find_root(v)
            if (a != b):
                parent[b] = a
        
        for u, v in connections:
            union(u, v)
        
        component_heaps = defaultdict(list)
        offline = set()

        for v in range(1, c+1):
            component_heaps[find_root(v)].append(v)
        
        for root in component_heaps:
            heapq.heapify(component_heaps[root])
        
        ans = []
        for query_type, v in queries:
            if query_type == 1:
                if v not in offline:
                    ans.append(v)
                else:
                    root = find_root(v)
                    heap = component_heaps[root]
                    
                    found = False
                    while heap:
                        top = heap[0]
                        if top not in offline:
                            ans.append(top)
                            found = True
                            break
                        heapq.heappop(heap)
                    
                    if not found:
                        ans.append(-1)
            else:
                offline.add(v)
        
        return ans