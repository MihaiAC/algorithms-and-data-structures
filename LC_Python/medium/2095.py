from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle base cases
        if head.next is None:
            return None

        if head.next.next is None:
            head.next = None
            return head

        slow = head.next
        fast = head.next.next
        prev = head

        while True:
            if fast.next is None:
                prev.next = slow.next
                break

            slow = slow.next
            prev = prev.next
            fast = fast.next.next

            if fast is None:
                prev.next = slow.next
                break

        return head
