from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        res = 0
        for comp in composition:
            l, r = 0, min(stock) + budget
            while l < r:
                m = (l + r) // 2 + 1
                spend = 0
                for i, cost_i in enumerate(cost):
                    spend += cost_i * max(0, (m * comp[i] - stock[i]))
                if spend > budget:
                    r = m - 1
                else:
                    l = m
            res = max(res, l)
        return res