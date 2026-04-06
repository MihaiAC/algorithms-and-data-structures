from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        currNode = head
        ans = []
        monoStack = []

        while currNode is not None:
            currVal = currNode.val

            while len(monoStack) > 0 and monoStack[-1][0] < currVal:
                _, idx = monoStack.pop()
                ans[idx] = currVal

            monoStack.append((currVal, len(ans)))
            ans.append(0)
            currNode = currNode.next

        return ans
