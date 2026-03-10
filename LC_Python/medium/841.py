from typing import List

from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        N = len(rooms)
        reached = set()
        reached.add(0)
        queue.appendleft(0)

        while len(queue) > 0:
            curr_room = queue.pop()

            for room_key in rooms[curr_room]:
                if room_key in reached:
                    continue
                else:
                    queue.appendleft(room_key)
                    reached.add(room_key)
        
        return len(reached) == N



if __name__ == '__main__':
    sol = Solution()
    rooms = [[1],[2],[3],[]]
    print(sol.canVisitAllRooms(rooms))