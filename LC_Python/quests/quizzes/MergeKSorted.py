from typing import List, Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = None
        curr = None
        heap = []
        for idx, node in enumerate(lists):
            if node is not None:
                heappush(heap, (node.val, idx))

        while len(heap) > 0:
            curr_val, node_idx = heappop(heap)
            if lists[node_idx].next is not None:
                lists[node_idx] = lists[node_idx].next
                heappush(heap, (lists[node_idx].val, node_idx))

            if root is not None:
                curr.next = ListNode(curr_val)
                curr = curr.next
            else:
                root = ListNode(curr_val)
                curr = root

        return root


# sol = Solution()
# l1 = ListNode.from_list([1, 4, 5])
# l2 = ListNode.from_list([1, 3, 4])
# l3 = ListNode.from_list([2, 6])
# print(sol.mergeKLists([l1, l2, l3]).to_list())
