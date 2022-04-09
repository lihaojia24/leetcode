
# Definition for a Node.
from collections import deque
from typing import List


class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

# 递归
class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    ans = []
    def helper(node):
      if not node: return
      for child in node.children:
        helper(child)
      ans.append(node.val)
    helper(root)
    return ans

# 迭代
class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    ans = []
    q = deque([root])
    while q and q[-1]:
      node = q.popleft()
      ans.append(node.val)
      # for i in range(len(node.children)):
      #   q.appendleft(i)
      q.extendleft(node.children)
    return ans[::-1]
