from typing import List

class Solution:
  def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    l = len(original)
    if l != m * n:
      return []
    res = [[0] * n for _ in range(m)]
    index = 0
    for i in range(m):
      for j in range(n):
        res[i][j] = original[index]
        index += 1
    return res