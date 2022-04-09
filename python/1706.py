from typing import List

class Solution:
  def findBall(self, grid: List[List[int]]) -> List[int]:
    n  = len(grid[0])
    balls = [i for i in range(n)]
    for row in grid:
      for i, ball in enumerate(balls):
        if -1 == ball:
          continue
        if row[ball] == 1 and ball < n - 1 and row[ball + 1] == 1:
          balls[i] += 1
        elif row[ball] == -1 and ball > 0 and row[ball - 1] == -1:
          balls[i] -= 1
        else:
          balls[i] = -1
    return balls

grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
s = Solution()
print(s.findBall(grid))