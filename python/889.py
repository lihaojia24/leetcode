from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        node_val = preorder[0]
        left_root_val = preorder[1]
        i = 0
        while postorder[i] != left_root_val: i += 1
        left_preorder = preorder[1:i+2]
        right_preorder = preorder[i+2:]
        left_posorder = postorder[:i+1]
        right_postorder = postorder[i+1:-1]
        return TreeNode(node_val, self.constructFromPrePost(left_posorder, left_posorder), self.constructFromPrePost(right_preorder, right_postorder))
        

