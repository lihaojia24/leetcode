from collections import deque
from typing import List

class Solution:
  def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    if len(blocked) < 2:
      return True
    
    BOUNDARY = 10**6

    # 简化棋盘
    rIndex = sorted(set(pos[0] for pos in blocked) | {source[0], target[0]})
    cIndex = sorted(set(pos[1] for pos in blocked) | {source[1], target[1]})
    rMap = dict()
    cMap = dict()

    rId = 0 if rIndex[0] == 0 else 1
    rMap[rIndex[0]] = rId
    for i in range(1, len(rIndex)):
      rId += 1 if rIndex[i] == rIndex[i - 1] + 1 else 2
      rMap[rIndex[i]] = rId
    if rIndex[-1] != BOUNDARY - 1:
      rId += 1

    cId = 0 if cIndex[0] == 0 else 1
    cMap[cIndex[0]] = cId
    for i in range(1, len(cIndex)):
      cId += 1 if cIndex[i] == cIndex[i - 1] + 1 else 2
      cMap[cIndex[i]] = cId
    if cIndex[-1] != BOUNDARY - 1:
      cId += 1

    grid = [[0] * (cId + 1) for _ in range(rId + 1)]

    for pos in blocked:
      grid[rMap[pos[0]]][cMap[pos[1]]] = 1

    start = [rMap[source[0]], cMap[source[1]]]
    print(start)
    end = [rMap[target[0]], cMap[target[1]]]

    q = deque()
    q.append(start)
    grid[start[0]][start[1]] = 1
    while q:
      node = q.popleft()
      print(node)
      x, y = node
      for tx, ty in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= tx <= rId and 0 <= ty <= cId and grid[tx][ty] != 1:
          if (tx, ty) == (end[0], end[1]):
            return True
          grid[tx][ty] = 1
          q.append([tx, ty])
    return False
