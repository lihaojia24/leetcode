from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, rows, cols = len(arr) + 1, len(mat), len(mat[0])
        n2row = [0] * n
        n2col = [0] * n
        row2F = [0] * rows
        col2F = [0] * cols
        for row in range(rows):
            for col in range(cols):
                num = mat[row][col]
                n2row[num] = row
                n2col[num] = col
        for i, num in enumerate(arr):
            row2F[n2row[num]] += 1
            col2F[n2col[num]] += 1
            if row2F[n2row[num]] == cols or col2F[n2col[num]] == rows:
                return i
        return n - 2