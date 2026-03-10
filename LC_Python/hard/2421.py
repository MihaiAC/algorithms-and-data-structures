from typing import List


class Solution:
    # 1st idea: bottom up.
    # 2nd idea, if 1 doesn't work: special algorithm for line case + detection.
    # 3rd idea: DSU.
    
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        neighbors = dict()
        leaves = set()
        for u, v in edges:
            if u in neighbors:
                neighbors[u].append(v)
                leaves.discard(u)
            else:
                neighbors[u] = [v]
                leaves.add(u)
        
            if v in neighbors:
                neighbors[v].append(u)
                leaves.discard(v)
            else:
                neighbors[v] = [u]
                leaves.add(v)
        
        if len(edges) == 0:
            return 1
        elif len(edges) == 1:
            if vals[0] == vals[1]:
                return 3
            else:
                return 2
        
        number_of_paths = 0
        
        paths = dict()
        parents = set()

        N = len(vals)
        for leaf in leaves:
            paths[leaf] = dict()
            paths[leaf][vals[leaf]] = 1
            parents.add(neighbors[leaf][0])
            number_of_paths += 1


        while len(leaves) != N:
            new_parents = set()

            # Merge leaves.
            for parent in parents:
                number_of_paths += 1
                nr_paths = dict()
                nr_paths[vals[parent]] = 1
                for neighbor in neighbors[parent]:
                    if neighbor not in leaves:
                        new_parents.add(neighbor)
                    else:
                        child_dict = paths[neighbor]

                        # Merge dictionaries.
                        for value in child_dict:
                            print(vals[parent])
                            print(value)
                            if vals[parent] > value:
                                continue
                            else:
                                if value in nr_paths:
                                    number_of_paths += child_dict[value] * nr_paths[value]
                                    nr_paths[value] += child_dict[value]
                                else:
                                    nr_paths[value] = child_dict[value]
                        del paths[neighbor]
                
                paths[parent] = nr_paths
            
            leaves = leaves.union(parents)
            parents = new_parents
        
        return self.number_of_paths