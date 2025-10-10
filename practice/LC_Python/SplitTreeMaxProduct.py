from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def calculateAllSums(root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_sum = Solution.calculateAllSums(root.left)
        right_sum = Solution.calculateAllSums(root.right)

        root.val = (root.val, left_sum, right_sum)

        return left_sum + right_sum + root.val[0]
    
    @staticmethod
    def calculateMaxProduct(root: Optional[TreeNode], sum_ancestors: int) -> int:
        if root is None:
            return 0

        prod_cut_left = root.val[1] * (sum_ancestors + root.val[2] + root.val[0])
        prod_cut_right = root.val[2] * (sum_ancestors + root.val[1] + root.val[0])

        max_product_left = Solution.calculateMaxProduct(root.left, sum_ancestors + root.val[0] + root.val[2])
        max_product_right = Solution.calculateMaxProduct(root.right, sum_ancestors + root.val[0] + root.val[1])

        return max(prod_cut_left, prod_cut_right, max_product_left, max_product_right)


    def maxProduct(self, root: Optional[TreeNode]) -> int:
        Solution.calculateAllSums(root)

        return Solution.calculateMaxProduct(root, 0)


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(3), TreeNode(6))

    sol = Solution()
    print(sol.maxProduct(tree))
    print(tree.val)