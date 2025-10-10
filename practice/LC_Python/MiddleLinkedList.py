from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def createFromList(vals: List[int]):
        head = ListNode(val=vals[0])
        tail = head
        for val in vals[1:]:
            tail.next = ListNode(val=val, next=None)
            tail = tail.next
        return head   

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        parser = head
        double_parser = head
        while True:
            double_parser = double_parser.next
            if double_parser is None:
                return parser.val

            double_parser = double_parser.next
            if double_parser is None:
                return parser.next.val
            
            parser = parser.next


if __name__ == '__main__':
    sol = Solution()
    vals = [1, 2, 3, 4, 5, 6]
    head = ListNode.createFromList(vals)
    print(sol.middleNode(head))