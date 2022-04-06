from collections import deque
from typing import List

class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    ans = set(range(n))
    count = [0] * n
    linkNode = [[] for _ in range(n)]
    for edge in edges:
      linkNode[edge[0]].append(edge[1])
      linkNode[edge[1]].append(edge[0])
      count[edge[0]] += 1
      count[edge[1]] += 1
    while len(ans) > 2:
      delset = []
      for i in range(n):
        if count[i] == 1:
          ans.discard(i)
          delset.append(i)
      for node in delset:
        for lnode in linkNode[node]:
          count[lnode] -= 1
          count[node] -= 1
      # 构建映射 降低复杂度
      # for edge in edges:
      #   if edge[0] in delset or edge[1] in delset:
      #     count[edge[0]] -= 1
      #     count[edge[1]] -= 1
      # print(count)
    return list(ans)
  
class Solution1:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x
        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]

s = Solution()
n = 8
edges = [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]]
print(s.findMinHeightTrees(n, edges))