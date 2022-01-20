# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool: 
      level = 0
      stack = [root]
      while stack:
        tmp = []
        n = len(stack)
        for i in range(n):
          if level % 2 == 1 :
            if stack[i].val % 2 == 1 :
              return False
            if i > 0 and stack[i].val >= stack[i - 1].val:
              return False
          if level % 2 == 0:
            if stack[i].val % 2 == 0 :
              return False
            if i > 0 and stack[i].val <= stack[i - 1].val:
              return False
          if stack[i].left:
            tmp.append(stack[i].left)
          if stack[i].right:
            tmp.append(stack[i].right)
        level += 1
        stack = tmp
      return True
