from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0: return None
        node_val = postorder[-1]
        i = 0
        while inorder[i] != node_val: i = i+1
        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]
        left_postorder = postorder[:i]
        right_postorder = postorder[i:-1]
        node = TreeNode()
        node.val = node_val
        node.left = self.buildTree(left_inorder, left_postorder)
        node.right = self.buildTree(right_inorder, right_postorder)
        return node