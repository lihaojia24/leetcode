# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if node is None:
                return 0, 0
            lr, lnr = dfs(node.left)
            rr, rnr = dfs(node.right)
            r = lnr + rnr + node.val
            nr = max(lr,lnr) + max(rr, rnr)
            return r, nr
        return max(dfs(root))