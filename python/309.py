from functools import cache
from typing import List
from math import inf

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i: int, hold: bool) -> int:
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-2, False) - prices[i])
            return max(dfs(i-1, False), dfs(i-1, True) + prices[i])
        return dfs(n-1, False)
    
    def maxProfit(self, prices: List[int]) -> int:
        pnHold, nhold, hold = 0, 0, -inf
        for price in prices:
            pnHold, nhold, hold = nhold, max(nhold, hold + price), max(hold, pnHold - price)
        return nhold
