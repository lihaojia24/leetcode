from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return None
        root_val = preorder[0]
        i = 0
        for i in range(len(inorder)):
            if inorder[i] == root_val: break
        left_preorder = preorder[1:i+1]
        right_preorder = preorder[i+1:]
        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]
        node = TreeNode(root_val)
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)
        return node