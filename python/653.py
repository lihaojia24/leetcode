from collections import deque
from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def create_BTree(nodes: List[int]) -> TreeNode:
  root = TreeNode()
  q = deque([root])
  for i in range(len(nodes)):
    node = q.popleft()
    left, right = TreeNode(), TreeNode()
    q.append(left)
    q.append(right)
    node.left = left
    node.right = right
    node.val = nodes[i]
  return root

def print_BTree(root: TreeNode):
  q = deque([root])
  ans = []
  while q:
    node = q.popleft()
    ans.app 

class Solution:
  def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    def find(k: int) -> bool:
      node = root
      while node:
        if node.val == k:
          return True
        elif node.val < k:
          if node.right:
            node = node.right
          else:
            return False
        elif node.val > k:
          if node.left:
            node = node.left
          else:
            return False
      return False
    
    def dfs(node: TreeNode):
      if node: print(node.val)
      if node != None:
        if k != 2 * node.val and find(k - node.val): return True
        elif dfs(node.left): return True
        elif dfs(node.right): return True
        else: return False
      else: return False
    
    return dfs(root)
    