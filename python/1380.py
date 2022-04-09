from typing import List

class Solution:
  def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
    ans = []
    maxRow = [min(row) for row in matrix]
    minCol = [max(col) for col in zip(*matrix)]
    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        if matrix[row][col] == maxRow[row] == minCol[col]:
          ans.append(matrix[row][col])
    return ans
