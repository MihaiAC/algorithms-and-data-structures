from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_indices = []
        prev_val = head.val
        curr = head.next
        idx = 1
        min_dist = 10**5 + 1

        while curr is not None:
            if curr.next is None:
                break

            if (
                prev_val < curr.val > curr.next.val
                or prev_val > curr.val < curr.next.val
            ):
                if len(critical_indices) > 0:
                    min_dist = min(min_dist, idx - critical_indices[-1])
                critical_indices.append(idx)

            idx += 1
            prev_val = curr.val
            curr = curr.next

        if len(critical_indices) < 2:
            return [-1, -1]

        return [min_dist, critical_indices[-1] - critical_indices[0]]
