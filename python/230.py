# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        tmp = root
        while stack or tmp:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            k -= 1
            if 0 == k:
                return tmp.val
            tmp = tmp.right

