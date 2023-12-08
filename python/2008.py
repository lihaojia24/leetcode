from typing import List

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        g = [[] for _ in range(n+1)]
        for x, y, tip in rides:
            g[y].append([x, tip])
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            for x, tip in g[i]:
                dp[i] = max(dp[i], dp[x]+i-x+tip)
        return dp[-1]