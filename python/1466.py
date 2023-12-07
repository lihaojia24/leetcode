from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for f, t in connections:
            g[f].append([t, False])
            g[t].append([f, True])
        ans = 0
        def dfs(root: int, fa: int) -> None:
            nonlocal ans
            for x in g[root]:
                if x[0] != fa:
                    if not x[1]:
                        ans += 1
                    dfs(x[0], root)
        dfs(0, -1)
        return ans