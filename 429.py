
# Definition for a Node.
from typing import List


class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children


class Solution:
  def levelOrder(self, root: 'Node') -> List[List[int]]:
    if root:
      q = [root]
      ans = []
      while q:
        n = len(q)
        ans.append([node.val for node in q])
        for i in range(n):
          for child in q[i].children:
            q.append(child)
        q = q[n:]
      return ans
    return []
