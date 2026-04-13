from typing import List, Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other: ListNode):
        return self.val < other.val

    @staticmethod
    def from_list(nums: int) -> Optional[ListNode]:
        if len(nums) == 0:
            return None

        head = ListNode(nums[0])
        curr = head
        for num in nums[1:]:
            curr.next = ListNode(num)
            curr = curr.next

        return head

    def to_list(self) -> List[int]:
        nums = []

        head = self
        while head is not None:
            nums.append(head.val)
            head = head.next

        return nums


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = None
        curr = None
        heap = []
        for node in lists:
            if node is not None:
                heappush(heap, node)

        while len(heap) > 0:
            curr_node = heappop(heap)
            if curr_node.next is not None:
                heappush(heap, curr_node.next)

            if root is not None:
                curr.next = ListNode(curr_node.val)
                curr = curr.next
            else:
                root = ListNode(curr_node.val)
                curr = root

        return root


sol = Solution()
l1 = ListNode.from_list([1, 4, 5])
l2 = ListNode.from_list([1, 3, 4])
l3 = ListNode.from_list([2, 6])
print(sol.mergeKLists([l1, l2, l3]).to_list())
