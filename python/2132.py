import copy
from typing import List

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                preSum[i][j] = grid[i-1][j-1] - preSum[i-1][j-1] + preSum[i][j-1] + preSum[i-1][j] 
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 2 - stampHeight):
            for j in range(1, n + 2 - stampWidth):
                x = i + stampHeight - 1
                y = j + stampWidth - 1
                if preSum[x][y] + preSum[i-1][j-1] - preSum[i-1][y] - preSum[x][j-1] == 0:
                    diff[i][j] += 1
                    diff[x+1][y+1] += 1
                    diff[i][y+1] -= 1
                    diff[x+1][j] -= 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diff[i][j] = diff[i][j] - diff[i-1][j-1] + diff[i-1][j] + diff[i][j-1] 
                if grid[i-1][j-1] == 0 and diff[i][j] == 0:
                    return False
        return True
