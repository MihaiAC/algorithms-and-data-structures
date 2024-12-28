from typing import Optional, Iterator

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def leafIterator(root: Optional[TreeNode]):
        if root.left is not None:
            yield from Solution.leafIterator(root.left)
        
        if root.right is not None:
            yield from Solution.leafIterator(root.right)
        
        if root.left is None and root.right is None:
            yield root.val


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1_iterator = Solution.leafIterator(root1)
        tree2_iterator = Solution.leafIterator(root2)
        tree1_end = False
        tree2_end = False

        while True:
            try:
                elem1 = next(tree1_iterator)
            except StopIteration:
                tree1_end = True
            
            try:
                elem2 = next(tree2_iterator)
            except StopIteration:
                tree2_end = True
            
            if tree1_end or tree2_end:
                return tree1_end == tree2_end

            if elem1 != elem2:
                return False        

if __name__ == '__main__':
    sol = Solution()

    tree1 = TreeNode(0, TreeNode(1), TreeNode(2))
    tree2 = TreeNode(0, TreeNode(2), TreeNode(1))

    print(sol.leafSimilar(tree1, tree2))