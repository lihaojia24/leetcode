from math import ceil
from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        EPS = 1e-7
        n = len(dist)
        dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.
        for i in range(1, n+1):
            for j in range(i+1):
                if j != i:
                    dp[i][j] = min(dp[i][j], ceil(dp[i-1][j] + dist[i-1] / speed - EPS))
                if j != 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + dist[i-1] / speed)
        for j in range(n + 1):
            if dp[n][j] < hoursBefore + EPS:
                return j
        return -1