from typing import List

class Solution:
  def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    rowsMax = [0] * m
    colsMax = [0] * n
    for i in range(m):
      for j in range(n):
        rowsMax[i] = max(rowsMax[i], grid[i][j])
        colsMax[j] = max(colsMax[j], grid[i][j])
    ans = 0
    for i in range(m):
      for j in range(n):
        ans += min(rowsMax[i], colsMax[j]) - grid[i][j]
    return ans
