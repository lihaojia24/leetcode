# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, ma, mi):
            if root == None:
                return 0
            diff = max(abs(root.val - ma), abs(root.val - mi))
            ma = max(ma, root.val)
            mi = min(mi, root.val)
            return max(diff, dfs(root.left, ma, mi), dfs(root.right, ma, mi))
        return dfs(root, root.val, root.val)