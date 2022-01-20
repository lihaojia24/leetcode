from collections import deque
from typing import List

# DFS
class Solution:
  def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    graph = [[] for _ in range(n)]
    ans = [-1] * n

    # init graph
    for richer, poorer in richer:
      graph[poorer].append(richer)

    def dfs(index: int):
      if ans[index] != -1:
        return
      ans[index] = index
      for richer in graph[index]:
        dfs(richer)
        if quiet[ans[richer]] < quiet[ans[index]]:
          ans[index] = ans[richer]
    
    for index in range(n):
      dfs(index)
    
    return ans

# Topological Sorting
class Solution:
  def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    n = len(quiet)
    graph = [[] for _ in range(n)]
    inDeg = [0] * n
    
    # init graph
    for richer, poorer in richer:
      graph[richer].append(poorer)
      inDeg[poorer] += 1

    ans = list(range(n))

    q = deque(i for i, deg in enumerate(inDeg) if deg == 0)

    while q:
      index = q.popleft()
      for poorer in graph[index]:
        if quiet[ans[index]] < quiet[ans[poorer]]:
          ans[poorer] = ans[index]
        inDeg[poorer] -= 1
        if inDeg[poorer] == 0:
          q.append(poorer)
    return ans


    