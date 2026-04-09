import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path


class Solution:
    def __init__(self, input_file: str):
        lines = open(input_file).read().strip().split("\n")

        self.graph = nx.Graph()
        for line in lines:
            u, v = line.split("-")
            self.graph.add_edge(u, v)

    def find_max_len_clique(self) -> str:
        longest_clique = list(nx.approximation.max_clique(self.graph))
        longest_clique.sort()
        return ",".join(longest_clique)

    def visualize(self, clique: set):
        node_colors = [
            "red" if n in clique else "steelblue" for n in self.graph.nodes()
        ]
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(
            self.graph,
            pos,
            node_color=node_colors,
            with_labels=True,
            node_size=200,
            font_size=7,
        )
        plt.title("Max clique nodes in red")
        plt.show()


if __name__ == "__main__":
    sol = Solution(Path(__file__).parent / "input")
    clique_str = sol.find_max_len_clique()
    print(clique_str)
    sol.visualize(set(clique_str.split(",")))
