from collections import defaultdict
from sys import maxsize
from typing import List


class Solution:
  def checkWays(self, pairs: List[List[int]]) -> int:
    links = defaultdict(set)
    for x, y in pairs:
      links[x].add(y)
      links[y].add(x)
    root = next(( node for node, linkers in links.items() if len(linkers) == len(links) - 1), -1)
    if root == -1:
      return 0
    
    ans = 1

    for node, linkers in links.items():
      if node == root:
        continue

      curNum = len(linkers)
      parent = -1
      parentNum = maxsize

      for linker in linkers:
        if curNum <= len(links[linker]) < parentNum:
          parent = linker
          parentNum = len(links[linker]) 
      
      if parent == -1 or any(linker != parent and linker not in links[parent] for linker in linkers):
        return 0
      
      if curNum == parentNum:
        ans = 2
      
    return ans

s = Solution()
pairs = [[1,2],[2,3],[2,4],[1,5]]
ans = s.checkWays(pairs)
print(ans)