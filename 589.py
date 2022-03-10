from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# 递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
      ans = []
      self.helper(root, ans)
      return ans

    def helper(self, node, ans):
      if node:
        ans.append(node.val)
        for ch in node.children:
          self.helper(ch, ans)

from collections import deque
# 迭代
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
      q = deque([root])
      ans = []
      while q:
        node = q.popleft()
        ans.append(node.val)
        for i in range(len(node.children)):
          q.appendleft(node.children[len(node.children) - i - 1])
      return ans
