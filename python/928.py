from collections import Counter
from typing import List

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        st = set(initial)
        vis = [False] * len(graph)
        def dfs(x: int) -> None:
            vis[x] = True
            nonlocal size, node_id
            size+=1
            for y, conn in enumerate(graph[x]):
                if conn == 0:
                    continue
                if y in st:
                    if node_id != -2 and node_id != y:
                        node_id = y if node_id == -1 else -2
                elif not vis[y]:
                    dfs(y)
        cnt = Counter()
        for i, seen in enumerate(vis):
            if seen or i in st:
                continue
            node_id = -1
            size = 0
            dfs(i)
            if node_id >= 0:
                cnt[node_id] += size
        return min((-size, node_id) for node_id, size in cnt.items())[1] if cnt else min(initial)
        
