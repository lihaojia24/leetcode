from typing import List

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = [[] for _ in range(len(roads) + 1)]
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)
        ans = 0
        def dfs(root: int, fa: int) -> int:
            size = 1
            for x in g[root]:
                if x != fa:
                    size += dfs(x, root)
            nonlocal ans
            ans += (size-1)/seats + 1
            return size
        for x in g[0]:
            dfs(x, 0)
        return ans
