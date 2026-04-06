from typing import Optional, List
from heapq import heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        heap = []
        currNode = head
        ans = []

        while currNode is not None:
            currVal = currNode.val

            while len(heap) > 0 and heap[0][0] < currVal:
                _, idx = heappop(heap)
                ans[idx] = currVal

            heappush(heap, (currVal, len(ans)))
            ans.append(0)
            currNode = currNode.next

        return ans
