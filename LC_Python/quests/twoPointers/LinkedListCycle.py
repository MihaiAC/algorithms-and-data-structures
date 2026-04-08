from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        single = head.next
        double = head.next.next

        while single != double and double is not None:
            single = single.next
            double = double.next
            if double is not None:
                double = double.next

        return single == double
