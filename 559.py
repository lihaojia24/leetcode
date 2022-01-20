
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# dfs
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        return 1 + max((self.maxDepth(node) for node in root.children), default = 0)

# bfs
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        queue = [root]
        ans = 0
        while queue:
            queue = [child for node in queue for child in node.children]
            ans += 1
        return ans