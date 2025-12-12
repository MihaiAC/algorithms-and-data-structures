from typing import List
import heapq


class Solution:
    def countMentions(self, N: int, events: List[List[str]]) -> List[int]:
        online = set(range(N))
        offline = []
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))

        ans = [0] * N
        base_inc = 0
        for event_type, timestamp, target in events:
            timestamp = int(timestamp)

            while offline and offline[0][0] <= timestamp:
                _, user = heapq.heappop(offline)
                online.add(user)

            if event_type == "MESSAGE":
                if target == "ALL":
                    base_inc += 1
                elif target == "HERE":
                    for user in online:
                        ans[user] += 1
                else:
                    for id_user in target.split(" "):
                        ans[int(id_user[2:])] += 1
            else:
                user = int(target)
                heapq.heappush(offline, (int(timestamp) + 60, user))

                if user in online:
                    online.remove(user)

        return [x + base_inc for x in ans]
