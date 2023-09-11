# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def depth(node: Optional[TreeNode]) -> int:
            if node == None: return 0
            return 1 + max(depth(node.right), depth(node.left))
        left = depth(root.left)
        right = depth(root.right)
        if left == right: return root
        elif left > right: return self.lcaDeepestLeaves(root.left)
        else: return self.lcaDeepestLeaves(root.right)