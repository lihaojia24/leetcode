class Solution:
  def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    dp = [[1] * n for _ in range(n)]
    for step in range(1, k + 1):
      dpTmp = [[0] * n for _ in range(n)]
      for x in range(n):
        for y in range(n):
          for dx, dy in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
            tx = x + dx
            ty = y + dy
            if 0 <= tx < n and 0 <= ty < n:
              dpTmp[x][y] += dp[tx][ty] / 8
      dp = dpTmp
    return dp[row][column]

n = 3 
k = 2
row = 0
column = 0
s = Solution()
print(s.knightProbability(n,k,row,column))