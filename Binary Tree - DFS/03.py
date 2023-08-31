# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        n = 0

        def helper(root: TreeNode, mx: int):
            nonlocal n
            if mx <= root.val:
                mx = root.val
                n += 1
            if root.left:
                helper(root.left, mx)
            if root.right:
                helper(root.right, mx)

        helper(root, root.val)
        return n


t = TreeNode(
    3,
    TreeNode(
        1,
        TreeNode(3),
    ),
    TreeNode(4, TreeNode(1), TreeNode(5)),
)
print(Solution().goodNodes(t))
