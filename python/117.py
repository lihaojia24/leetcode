
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return None
        q = [root]
        while q:
            for i in range(len(q) - 1):
                q[i].next = q[i+1]
            tmp = q
            q = []
            for node in tmp:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root