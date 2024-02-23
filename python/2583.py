# class Solution:
#     def passThePillow(self, n: int, time: int) -> int:
#         times = time // (n - 1)
#         res = time % (n - 1)
#         if times % 2:
#             return n - res
#         return res + 1

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def helper(node: TreeNode, level: int):
            if node == None: return
            if len(res) <= level:
                res.append(node.val)
            else:
                res[level] += node.val
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        if len(res) < k: return -1
        res.sort(reverse=True)
        return res[k-1]
