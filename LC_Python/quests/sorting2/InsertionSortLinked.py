from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head.next
        head.next = None

        while currNode is not None:
            nextNode = currNode.next
            currNode.next = None

            if currNode.val < head.val:
                currNode.next = head
                head = currNode
            else:
                iterNode = head
                while iterNode.next is not None and iterNode.next.val < currNode.val:
                    iterNode = iterNode.next

                if iterNode.next is None:
                    iterNode.next = currNode
                else:
                    currNode.next = iterNode.next
                    iterNode.next = currNode

            currNode = nextNode

        return head
