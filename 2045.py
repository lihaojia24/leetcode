from collections import deque
from dis import dis
from os import times
from typing import List

class Solution:
  def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
    graph = [[] for _ in range(n + 1)]
    for x, y in edges:
      graph[x].append(y)
      graph[y].append(x)
    q = deque([(1, 0)])
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[1][0] = 0
    while dist[n][1] == float('inf'):
      point, step = q.popleft()
      step += 1
      for nb in graph[point]:
        if dist[nb][0] == float('inf'):
          dist[nb][0] = step
          q.append((nb, step))
        elif dist[nb][1] == float('inf') and step != dist[nb][0]:
          dist[nb][1] = step
          q.append((nb, step))
    ans = 0
    for _ in range(dist[n][1]):
      if ans % (change * 2) >= change:
        ans += change * 2 - ans % (change * 2)
      ans += time
    return ans