from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hasParent = set()
        valToNode = dict()

        for parent, child, is_left in descriptions:
            if parent not in valToNode:
                valToNode[parent] = TreeNode(parent)
            parentNode = valToNode[parent]

            if child not in valToNode:
                valToNode[child] = TreeNode(child)
            childNode = valToNode[child]

            if is_left:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

            hasParent.add(child)

        for val in valToNode.keys():
            if val not in hasParent:
                return valToNode[val]

        return None
