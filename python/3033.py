from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix[0])
        max_col = [0] * len(n)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_col[j] = max(max_col[j], matrix[i][j])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_col[j]
        return matrix