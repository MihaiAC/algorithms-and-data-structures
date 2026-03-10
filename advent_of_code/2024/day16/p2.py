import networkx as nx

class Solution:
    def __init__(self, input_file: str):
        self.matrix = open(input_file).read().strip().split('\n')
        self.DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.COMPLEMENTS = {
            (-1, 0): [(0, 1), (0, -1)], 
            (0, -1): [(1, 0), (-1, 0)], 
            (0, 1): [(1, 0), (-1, 0)], 
            (1, 0): [(0, 1), (0, -1)]
            }

        self.G = nx.DiGraph()

        # Add nodes.
        for ii, row in enumerate(self.matrix):
            for jj, val in enumerate(row):
                if val == '#':
                    continue
                elif val == 'S':
                    self.start_coords = (ii, jj)
                elif val == 'E':
                    self.end_coords = (ii, jj)
                
                for delta in self.DELTAS:
                    self.G.add_node((ii, jj, delta))
        
        # Add edges.
        for (ii, jj, delta) in self.G.nodes:
            if (ii+delta[0], jj+delta[1], delta) in self.G.nodes:
                self.G.add_edge((ii, jj, delta), (ii+delta[0], jj+delta[1], delta), weight=1)
            for complement_delta in self.COMPLEMENTS[delta]:
                self.G.add_edge((ii, jj, delta), (ii, jj, complement_delta), weight=1000)
        
        # Add edges from the target node to a special "end node".
        for delta in self.DELTAS:
            self.G.add_edge((self.end_coords[0], self.end_coords[1], delta), "end", weight=0)

    def calc_n_tiles(self) -> int:
        all_paths = nx.all_shortest_paths(self.G, (self.start_coords[0], self.start_coords[1], (0, 1)), "end", weight="weight")
        return len({(node[0], node[1]) for path in all_paths for node in path})-1
        

if __name__ == '__main__':
    sol = Solution('input')
    print(sol.calc_n_tiles())