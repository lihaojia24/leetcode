from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        target += 1
        cur = self.root
        for i in range(target.bit_length() - 2, -1, -1):
            bit = (target >> i) & 1
            if bit == 0:
                cur = cur.left
            else:
                cur = cur.right
            if cur == None:
                return False
        return True

# class FindElements:

#     def __init__(self, root: Optional[TreeNode]):
#         s = set()
#         def dfs(node: Optional[TreeNode], val: int) -> None:
#             if node is None:
#                 return
#             s.add(val)
#             dfs(node.left, val * 2 + 1)
#             dfs(node.right, val * 2 + 2)
#         dfs(root, 0)
#         self.s = s

#     def find(self, target: int) -> bool:
#         return target in self.s



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)