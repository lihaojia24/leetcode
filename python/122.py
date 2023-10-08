from functools import cache
from math import inf
from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-1, False) - prices[i])
            return max(dfs(i-1, False), dfs(i-1, True) + prices[i])
        return dfs(n-1, False)
    
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        dp[0][1] = -inf
        for i, price in enumerate(prices):
            dp[i+1][0] = max(dp[i][0], dp[i][1] + price)
            dp[i+1][1] = max(dp[i][1], dp[i][0] - price)
        return dp[n][0]
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = -inf
        nHold = 0
        for price in prices:
            new_hold = max(hold, nHold - price)
            nHold = max(nHold, hold + price)
            hold = new_hold
        return nHold