from typing import List
from collections import defaultdict, deque


# Following the editorial
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        def parents(mNode: int, cNode: int, turn: int):
            if turn == 1:
                for node in graph[cNode]:
                    if node > 0:
                        yield (mNode, node, 2)
            else:
                for node in graph[mNode]:
                    yield (node, cNode, 1)

        # state = (mouse node, cat node, turn)
        # maps state -> number of children that are draws
        draw_children_count = dict()
        for mNode in range(N):
            for cNode in range(N):
                draw_children_count[(mNode, cNode, 1)] = len(graph[mNode])
                draw_children_count[(mNode, cNode, 2)] = len(graph[cNode]) - (
                    0 in graph[cNode]
                )

        # outcome of a state: 1 = mouse wins, 2 = cat wins, 0 = draw
        winner = defaultdict(int)

        # all nodes that have a winner (trivially)
        queue = deque()
        for node in range(N):
            for turn in [1, 2]:
                # mouse at hole
                winner[(0, node, turn)] = 1
                queue.appendleft((0, node, turn, 1))

                # cat on mouse
                if node > 0:
                    winner[(node, node, turn)] = 2
                    queue.appendleft((node, node, turn, 2))

        # some kind of Dijkstra
        while len(queue) > 0:
            mNode, cNode, turn, outcome = queue.pop()
            for p_mNode, p_cNode, p_turn in parents(mNode, cNode, turn):
                # if adjacent state is not a draw => continue
                if winner[(p_mNode, p_cNode, p_turn)] != 0:
                    continue

                # if parent of the state can win => color this state as well + enqueue it
                if p_turn == outcome:
                    winner[(p_mNode, p_cNode, p_turn)] = outcome
                    queue.appendleft((p_mNode, p_cNode, p_turn, outcome))
                else:
                    draw_children_count[(p_mNode, p_cNode, p_turn)] -= 1
                    if draw_children_count[(p_mNode, p_cNode, p_turn)] == 0:
                        winner[(p_mNode, p_cNode, p_turn)] = 3 - p_turn
                        queue.append((p_mNode, p_cNode, p_turn, 3 - p_turn))

        return winner[(1, 2, 1)]


sol = Solution()
print(sol.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))
print(sol.catMouseGame([[1, 3], [0], [3], [0, 2]]))
print(sol.catMouseGame([[2, 3], [3, 4], [0, 4], [0, 1], [1, 2]]))
