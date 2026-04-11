from typing import List
from collections import defaultdict


class Solution:
    """Love that this is under DFS in LC Quests, but it's clearly a BFS problem."""

    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        friend_id: int,
        level: int,
    ) -> List[str]:
        n = len(friends)
        curr_nodes = {friend_id}
        curr_level = 0

        visited = [False] * n
        visited[friend_id] = True

        while curr_level < level and len(curr_nodes) > 0:
            next_nodes = set()
            for node in curr_nodes:
                for nxt in friends[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        next_nodes.add(nxt)
            curr_level += 1
            curr_nodes = next_nodes

        count = defaultdict(int)
        for node in curr_nodes:
            for video in watchedVideos[node]:
                count[video] += 1

        ans = sorted(list(count.keys()), key=lambda video: (count[video], video))
        return ans


sol = Solution()
print(
    sol.watchedVideosByFriends(
        [["A", "B"], ["C"], ["B", "C"], ["D"]], [[1, 2], [0, 3], [0, 3], [1, 2]], 0, 1
    )
)
print(
    sol.watchedVideosByFriends(
        [["A", "B"], ["C"], ["B", "C"], ["D"]], [[1, 2], [0, 3], [0, 3], [1, 2]], 0, 2
    )
)
