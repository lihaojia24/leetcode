# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == None:
            return None
        if original == target:
            return cloned
        res = self.getTargetCopy(original.left, cloned.left, target)
        if res != None:
            return res
        res = self.getTargetCopy(original.right, cloned.right, target)
        if res != None:
            return res
        return None