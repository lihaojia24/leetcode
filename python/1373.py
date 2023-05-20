# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    ans = 0
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        self.ans = 0
        def dfs(root: TreeNode) -> Tuple[bool, int, int, int]:
            isSearch = True
            res = root.val
            resmax = root.val
            resmin = root.val
            if root.left != None:
                lb, lval, lmax, lmin = dfs(root.left)
                resmin = min(lmin, resmin)
                resmax = max(lmax, resmax)
                if lmax >= root.val:
                    isSearch = False
                if lb:
                    res += lval
                else:
                    isSearch = False
            if root.right != None:
                rb, rval, rmax, rmin = dfs(root.right)
                resmin = min(rmin, resmin)
                resmax = max(rmax, resmax)
                if rmin <= root.val:
                    isSearch = False
                if rb:
                    res += rval
                else:
                    isSearch = False
            if isSearch and res > self.ans:
               self.ans = res
            return isSearch, res, resmax, resmin
        dfs(root)
        return self.ans
    
def f():
    
    def d():
        print(name)
    name = 'sss'
    d()

f()
                

