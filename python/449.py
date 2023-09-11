# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        def preOrder(root: Optional[TreeNode]):
            if root:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ','.join(vals)
                

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data or data == '':
            return None
        vals = list(map(int,data.split(',')))
        def help(vals: list[int]) -> Optional[TreeNode]:
            if len(vals) == 0: return None
            root = TreeNode(vals[0])
            lvals = [x for x in vals if x < vals[0]]
            rvals = [x for x in vals if x > vals[0]]
            root.left = help(lvals)
            root.right = help(rvals)
            return root
        return help(vals)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
tree = ser.serialize(root)
print(tree)
ans = deser.deserialize(tree)
print(ans.val)
print(ans.left.val)
print(ans.right.val)
