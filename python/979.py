# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: TreeNode):
            v = node.val
            n = 1
            if node.left:
                lv, ln = dfs(node.left)
                v += lv
                n += ln
            if node.right:
                rv, rn = dfs(node.right)
                v += rv
                n += rn
            nonlocal ans
            ans += abs(v - n)
            return v, n
        dfs(root)
        return ans