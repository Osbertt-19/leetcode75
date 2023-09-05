from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.mx = 0

        def traverse(root, i, n):
            if not root:
                return
            elif i == 1:
                traverse(root.left, 1, 1)
                traverse(root.right, 2, n + 1)
            elif i == 2:
                traverse(root.right, 2, 1)
                traverse(root.left, 1, n + 1)
            else:
                traverse(root.left, 1, n + 1)
                traverse(root.right, 2, n + 1)
            if self.mx < n:
                self.mx = n

        traverse(root, 0, 0)
        return self.mx


t = TreeNode(1)
t.right = TreeNode(1)
t.right.right = TreeNode(1)
t.right.left = TreeNode(1)
t.right.right.right = TreeNode(1)
t.right.right.left = TreeNode(1)
t.right.right.left.right = TreeNode(1)
t.right.right.left.right.right = TreeNode(1)

s = Solution()
print(s.longestZigZag(t))
