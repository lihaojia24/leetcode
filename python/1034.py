from collections import deque
from typing import List

# BFS
class Solution:
  def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    originalColor = grid[row][col]
    direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    border = []
    visited = [[False] * n for _ in range(m)]
    q = deque([(row, col)])
    while q:
      x, y = q.popleft()
      isBorder = False
      for dx, dy in direc:
        tx, ty = x + dx, y + dy
        if not (0 <= tx < m and 0 <= ty < n and grid[tx][ty] == originalColor):
          isBorder = True
        elif visited[tx][ty] == False:
          visited[tx][ty] = True
          q.append((tx, ty))
      if isBorder:
        border.append((x, y))
    for x, y in border:
      grid[x][y] = color
    return grid


# DFS
class Solution:
  def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
    border = []
    m = len(grid)
    n = len(grid[0])
    visited = [[False] * n for _ in range(m)]
    originalColor = grid[row][col]
    self.dfs(grid, row, col, originalColor, visited, border, m, n)
    for x, y in border:
      grid[x][y] = color
    return grid

  def dfs(self, grid, x, y, originalColor, visited, border, m, n):
    direc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    isBorder = False
    for dx, dy in direc:
      tx, ty = x + dx, y + dy
      if 0 <= tx < m and 0 <= ty < n and grid[tx][ty] == originalColor:
        if not visited[tx][ty]:
          visited[tx][ty] = True
          self.dfs(grid, tx, ty, originalColor, visited, border, m, n)
      else:
        isBorder = True
    if isBorder:
      border.append((x, y))

