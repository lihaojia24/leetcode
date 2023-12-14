from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(a: Optional[TreeNode], b: Optional[TreeNode], l: int):
            if a:
                if l % 2 == 1:
                    a.val, b.val = b.val, a.val
                helper(a.left, b.right, l+1)
                helper(a.right, b.left, l+1)
        helper(root.left, root.right, 1)
        return root