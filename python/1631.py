from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dp = [0] * cols
        for i in range(1, cols):
            dp[i] = max(dp[i-1], abs(heights[0][i] - heights[0][i-1]))
        for row in range(1, rows):
            dp[0] = max(dp[0], abs(heights[row][0] - heights[row-1][0]))
            for col in range(1, cols):
                m1 = max(dp[col], abs(heights[row][col] - heights[row-1][col]))
                m2 = max(dp[col-1], abs(heights[row][col] - heights[row][col-1]))
                dp[col] = max(m1, m2)        
        return dp[-1]
