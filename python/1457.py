# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode], mask=0) -> int:
        if root is None:
            return 0
        mask ^= 1 << root.val
        if root.left == root.right:
            return 1 if mask & (mask - 1) == 0 else 0
        return self.pseudoPalindromicPaths(root.left, mask) + self.pseudoPalindromicPaths(root.right, mask)
