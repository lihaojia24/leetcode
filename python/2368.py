from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        r_s = set(restricted)
        ans = 0
        def helper(node: int, fa: int):
            nonlocal ans
            if node in r_s: return
            ans+= 1
            for nxt in g[node]:
                if nxt != fa:
                    helper(nxt, node)
        helper(0, -1)
        return ans
