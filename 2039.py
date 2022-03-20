from collections import deque
from typing import List

class Solution:
  def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
    n = len(patience)
    paths = [[] for _ in range(n)]
    for node1, node2 in edges:
      paths[node1].append(node2)
      paths[node2].append(node1)
    length, viewed, nodes = 0, 1, deque([0])
    lengths = [-1] * n
    while viewed < n:
      length += 1
      for _ in range(len(nodes)):
        node = nodes.popleft()
        for path in paths[node]:
          if lengths[path] == -1 and path != 0:
            lengths[path] = length
            viewed += 1
            nodes.append(path)
    ans = 0
    print(lengths)
    for i in range(1, n):
      times = (lengths[i] * 2 - 1) // patience[i]
      time = lengths[i] * 2 + times * patience[i]
      if time > ans: ans = time
    return ans + 1
      
s = Solution()
edges = [[0,1],[0,2],[1,2]]
patience = [0,10,10]
print(s.networkBecomesIdle(edges, patience))