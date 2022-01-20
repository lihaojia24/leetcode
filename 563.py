# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self) -> None:
        self.ans = 0

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        sumLeft = self.dfs(node.left)
        sumRight = self.dfs(node.right)
        self.ans += abs(sumLeft - sumRight)
        return sumLeft + sumRight + node.val
    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans 