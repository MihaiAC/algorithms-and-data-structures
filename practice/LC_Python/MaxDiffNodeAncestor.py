from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    @staticmethod
    def maxAncestorDiffRec(root: Optional[TreeNode], min_ancestor: int, max_ancestor: int):
        if root is None:
            return max_ancestor-min_ancestor
        
        if root.val < min_ancestor:
            min_ancestor = root.val
        elif root.val > max_ancestor:
            max_ancestor = root.val
        
        return max(Solution.maxAncestorDiffRec(root.left, min_ancestor, max_ancestor), Solution.maxAncestorDiffRec(root.right, min_ancestor, max_ancestor))

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return Solution.maxAncestorDiffRec(root, root.val, root.val)


if __name__ == '__main__':
    sol = Solution()
    tree = TreeNode(val=1, left=TreeNode(2), right=TreeNode(10))

    print(sol.maxAncestorDiff(tree))