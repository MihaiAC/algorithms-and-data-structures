from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1:
            return TreeNode(inorder[0], None, None)

        rootVal = postorder[-1]
        idx = inorder.index(rootVal)
        return TreeNode(
            rootVal,
            self.buildTree(inorder[:idx], postorder[:idx]),
            self.buildTree(inorder[idx + 1 :], postorder[idx:-1]),
        )
