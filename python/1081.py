# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        limit = limit - root.val
        if root.left == None and root.right == None:
            return None if limit > 0 else root
        if root.left:
            root.left = self.sufficientSubset(root.left, limit)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit)
        if root.left or root.right:
            return root
        else:
            return None