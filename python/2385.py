from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        fa = {}
        start_node = None
        def dfs(node: Optional[TreeNode], from_: Optional[TreeNode]) -> None:
            if node is None:
                return
            fa[node] = from_  # 记录每个节点的父节点
            if node.val == start:  # 找到 start
                nonlocal start_node
                start_node = node
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        def maxDepth(node: Optional[TreeNode], from_: TreeNode) -> int:
            if node is None:
                return -1  # 注意这里是 -1，因为 start 的深度为 0
            return max(maxDepth(x, node) for x in (node.left, node.right, fa[node]) if x != from_) + 1
        return maxDepth(start_node, start_node)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/solutions/2753470/cong-liang-ci-bian-li-dao-yi-ci-bian-li-tmt0x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。