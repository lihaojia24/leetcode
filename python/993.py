from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def get_level_father(root: TreeNode, x: int) -> (int, int):
            q = [[root, -1]]
            level = -1
            while len(q) > 0:
                level += 1
                l = len(q)
                for _ in range(l):
                    node, father = q[0]
                    q = q[1:]
                    if node.val == x:
                        return level, father
                    if node.left != None:
                        q.append([node.left, node.val])
                    if node.right != None:
                        q.append([node.right, node.val])
            return -1, -1
        l1, f1 = get_level_father(root, x)
        l2, f2 = get_level_father(root, y)
        return l1 == l2 and f1 != f2
