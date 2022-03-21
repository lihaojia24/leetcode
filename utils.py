from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def create_BTree(nodes) -> TreeNode:
  n = len(nodes)
  if n == 0: return None
  root = TreeNode(val = nodes[0])
  q, i = deque([root]), 1
  while i < n:
    for _ in range(len(q)):
      node = q.popleft()
      if i < n and nodes[i]: 
        node.left = TreeNode(nodes[i])
        q.append(node.left)
      if i < n and nodes[i + 1]: 
        node.right = TreeNode(nodes[i+1])
        q.append(node.right)
      i += 2
  return root

def print_BTree(root: TreeNode):
  if root == None: print(None)
  ans = []
  q = deque([root])
  while len(q) > 0:
    if all([x == None for x in q]): break
    for _ in range(len(q)):
      node = q.popleft()
      print(node)
      if node:
        print(node.val, node.left, node.right)
      if node:
        ans.append(node.val)
        q.append(node.left)
        q.append(node.right)
      else:
        ans.append(None)
        q.append(None)
        q.append(None)
      
  print(ans)
      

if __name__ == '__main__':
  root = create_BTree([5,3,None,2,4,None,None])
  print_BTree(root)