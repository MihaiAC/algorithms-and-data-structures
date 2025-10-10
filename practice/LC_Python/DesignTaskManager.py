from collections import defaultdict
from typing import List
from heapq import heappush, heappop

class TaskManager:
    # With this approach, tasks with very low priority that have already
    # been deleted can stay in the heap indefinitely.
    # Periodic cleanup every N ops?
    def __init__(self, tasks: List[List[int]]):
        self.version = defaultdict(int)
        self.task_to_user = dict() # cleanup?
        self.heap = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.version[taskId] += 1
        self.task_to_user[taskId] = userId
        
        heappush(self.heap, (-priority, -taskId, userId, self.version[taskId]))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_to_user[taskId]
        self.version[taskId] += 1
        
        heappush(self.heap, (-newPriority, -taskId, userId, self.version[taskId]))

    def rmv(self, taskId: int) -> None:
        self.version[taskId] += 1
        
    def execTop(self) -> int:
        while True:
            if len(self.heap) == 0:
                return -1
            
            minus_prio, minus_taskId, userId, taskVer = heappop(self.heap)
            if taskVer < self.version[-minus_taskId]:
                continue
            else:
                return userId
            