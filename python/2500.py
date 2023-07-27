from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sorted_grid = [sorted(row) for row in grid]
        max_values = [max(col) for col in zip(*sorted_grid)]
        return sum(max_values)