from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        mx = float("-inf")
        lvl = 1
        x = 0
        while queue:
            sm = 0
            for q in queue:
                sm += q.val
            if mx < sm:
                mx = sm
                x = lvl
            temp = deque()
            while queue:
                current = queue.popleft()
                if current.left:
                    temp.append(current.left)
                if current.right:
                    temp.append(current.right)
            queue = temp
            lvl += 1
        return x
