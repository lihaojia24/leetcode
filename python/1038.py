# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0
        def helper(root: TreeNode) -> None:
            if root:
                nonlocal s
                helper(root.right)
                root.val += s
                s = root.val
                helper(root.left)
        helper(root)
        return root