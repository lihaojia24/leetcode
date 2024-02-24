from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node == None: return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        dfs(root)
        # st = []
        # while root != None or len(st) > 0:
        #     if root != None:
        #         st.append(root)
        #         root = root.left
        #     else:
        #         root = st[-1]
        #         st = st[:-1]
        #         nums.append(root.val)
        #         root = root.right
        def getBounds(target: int) -> List[int]:
            if target < nums[0]: return [-1, nums[0]]
            if target > nums[-1]: return [nums[-1], -1]
            l, r = 0, len(nums)-1
            while l < r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            if nums[l] == target: return [target, target]
            return [nums[l-1], nums[l]]
        ans = []
        for target in queries:
            ans.append(getBounds(target))
        return ans