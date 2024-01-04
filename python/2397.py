from typing import List

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        # m, n = len(matrix), len(matrix[0])
        masks = [sum(x << j for j, x in enumerate(row)) for row in matrix]
        ans = 0
        for subnet in range(1 << len(matrix[0])):
            if subnet.bit_count() == numSelect:
                covered_rows = sum( subnet & mask == mask for mask in masks)
                ans = max(ans, covered_rows)
        return ans