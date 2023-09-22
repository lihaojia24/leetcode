from typing import List

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        deg = list(map(len, g))
        left_edges = n - 1
        q = []
        for i, (c, d) in enumerate(zip(coins, deg)):
            if d == 1 and c == 0:
                q.append(i)
        while q:
            left_edges -= 1
            for y in g[q.pop()]:
                deg[y] -= 1
                if deg[y] == 1 and coins[y] == 0:
                    q.append(y)
        for i, (c, d) in enumerate(zip(coins, deg)):
            if d == 1 and c > 0:
                q.append(i)
        left_edges -= len(q)
        for x in q:
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1:
                    left_edges -= 1
        return left_edges * 2 if left_edges > 0 else 0
