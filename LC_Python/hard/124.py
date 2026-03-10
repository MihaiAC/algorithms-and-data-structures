from typing import Optional, Tuple, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def treeNodeBuilder(ls: List[int]) -> 'TreeNode':
        return TreeNode.treeNodeBuilderRec(ls, 0)
    
    @staticmethod
    def treeNodeBuilderRec(ls: List[int], idx: int) -> 'TreeNode':
        if idx >= len(ls):
            return None

        left_idx = 2*idx+1
        right_idx = 2*idx+2

        left_node = TreeNode.treeNodeBuilderRec(ls, left_idx)
        right_node = TreeNode.treeNodeBuilderRec(ls, right_idx)

        return TreeNode(ls[idx], left_node, right_node)
        

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxIgnoreNone(*args) -> int:
            maxInt = None
            for arg in args:
                if arg is None:
                    continue
                else:
                    if maxInt is None:
                        maxInt = arg
                    else:
                        maxInt = max(maxInt, arg)
            
            return maxInt
        
        def sumIgnoreNone(*args) -> int:
            sum_args = None
            for arg in args:
                if arg is not None:
                    if sum_args is None:
                        sum_args = arg
                    else:
                        sum_args += arg
            
            return sum_args

        def inner(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return (None, None)
            
            open_left, closed_left = inner(node.left)
            open_right, closed_right = inner(node.right)

            open_curr = maxIgnoreNone(node.val, sumIgnoreNone(node.val, open_left), sumIgnoreNone(node.val, open_right))
            closed_curr = maxIgnoreNone(node.val, open_left, open_right, closed_left, closed_right, open_curr, sumIgnoreNone(node.val, open_left, open_right))

            return (open_curr, closed_curr)
        
        return inner(root)[1]



if __name__ == '__main__':
    sol = Solution()
    
    ls = [1, 2, 3]
    tree = TreeNode.treeNodeBuilder(ls)

    print(tree.val)
    print(tree.left.val)
    print(tree.right.val)

    print(sol.maxPathSum(tree))