from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        odd_tail = head
        even_head = head.next
        even_tail = head.next

        while True:
            if even_tail.next is None:
                odd_tail.next = even_head
                return head
            
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next

            if odd_tail.next is None:
                odd_tail.next = even_head
                even_tail.next = None
                return head
            
            even_tail.next = odd_tail.next
            even_tail = even_tail.next




if __name__ == '__main__':
    sol = Solution()
    head = ListNode()
    tail = head
    head.val = 1
    for elem in [2, 3, 4, 5]:
        new_node = ListNode(val=elem)
        tail.next = new_node
        tail = new_node

    sol.oddEvenList(head)
