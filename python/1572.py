from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, ans = len(mat), 0
        for i in range(n):
            ans += mat[i][i]
            ans += mat[i][n-1-i]
        if n % 2:
            n >>= 1
            ans -= mat[n][n]
        return ans
    