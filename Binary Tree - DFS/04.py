from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        n = 0

        def helper(root, parents):
            if not root:
                return 0
            nonlocal n, targetSum
            sum = root.val
            if sum == targetSum:
                n += 1
            for i in range(len(parents)):
                sum += parents[i]
                if sum == targetSum:
                    n += 1
            if root.left:
                helper(root.left, [root.val] + parents)
            if root.right:
                helper(root.right, [root.val] + parents)

        helper(root, [])
        return n


t = TreeNode(
    3,
    TreeNode(
        1,
        TreeNode(3),
    ),
    TreeNode(4, TreeNode(1), TreeNode(5)),
)
