# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaves(root, leaves):
            if not root:
                return leaves
            if not root.right and not root.left:
                return leaves + [root.val]
            return findLeaves(root.left, leaves) + findLeaves(root.right, leaves)

        return findLeaves(root1, []) == findLeaves(root2, [])
