import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        preTree = collections.defaultdict(int)
        preTree[0] = 1

        def dfs(node: TreeNode, curr: int) -> int:
            res = 0
            if not node:
                return res
            curr += node.val
            res += preTree[curr - targetSum]
            preTree[curr] += 1
            res += dfs(node.left, curr)
            res += dfs(node.right, curr)
            preTree[curr] -= 1
            return res

        return dfs(root, 0)

