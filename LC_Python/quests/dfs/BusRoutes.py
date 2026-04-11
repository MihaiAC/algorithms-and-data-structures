from typing import List
from collections import defaultdict


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stopToBuses = defaultdict(set)
        for idx, route in enumerate(routes):
            for stop in route:
                stopToBuses[stop].add(idx)

        currStops = {source}
        visitedBuses = set()
        visitedStops = {source}
        buses = 0

        while len(currStops) > 0:
            buses += 1
            nextStops = set()

            for stop in currStops:
                for bus in stopToBuses[stop]:
                    if bus in visitedBuses:
                        continue
                    visitedBuses.add(bus)
                    for nxtStop in routes[bus]:
                        if nxtStop == target:
                            return buses
                        if nxtStop not in visitedStops:
                            visitedStops.add(nxtStop)
                            nextStops.add(nxtStop)

            currStops = nextStops

        return -1


sol = Solution()
print(sol.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
print(
    sol.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12)
)
