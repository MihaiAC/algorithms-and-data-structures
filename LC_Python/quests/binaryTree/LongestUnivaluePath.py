from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node: Optional[TreeNode], parent: int) -> int:
            if node is None:
                return 0

            left = helper(node.left, node.val)
            right = helper(node.right, node.val)

            nonlocal ans
            ans = max(ans, left + right)

            return max(left, right) + 1 if node.val == parent else 0

        helper(root, -1001)
        return ans
