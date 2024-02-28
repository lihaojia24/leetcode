from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range (n // 2, 0, -1):
            ans += abs(cost[2*i-1] - cost[2*i])
            cost[i-1] += max(cost[2*i-1], cost[2*i])
        return ans