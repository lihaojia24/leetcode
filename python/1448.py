# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def help(node: TreeNode, mx: int) -> int:
            ans = 0
            if node.val >= mx:
                ans += 1
                mx = node.val
            if node.left: ans += help(node.left, mx)
            if node.right: ans += help(node.right, mx)
            return ans
        ans = 0
        if root:
            ans += 1
            if root.left: ans += help(root.left, root.val)
            if root.right: ans += help(root.right, root.val)
        return ans
        # return ans
