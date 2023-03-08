from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        ans = [0] * (len(grid[0]) + 1)
        for row in grid:
            for i in range(len(ans)):
                ans[i+1] = max(ans[i], ans[i+1]) + row[i+1]
        return ans[-1]
