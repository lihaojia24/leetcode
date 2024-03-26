from cmath import inf
from functools import cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i: int, remain: int) -> int:
            if i < 0:
                return 0 if remain == 0 else inf
            if remain < coins[i]:
                return dfs(i - 1, remain)
            return min(dfs(i-1, remain), dfs(i, remain - coins[i]) + 1)
        ans = dfs(len(coins) - 1, amount)
        return ans if ans < inf else -1