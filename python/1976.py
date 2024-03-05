from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, d in roads:
            g[x].append([y, d])
            g[y].append([x, d])
        dones = [False] * n
        counts = [0] * n
        dists = [-1] * n
        dones[0] = True
        counts[0] = 1
        dists[0] = 0
        min_node = 0
        for _ in range(n-1):
            for nxt, d in g[min_node]:
                if dones[nxt]: continue
                if dists[nxt] == -1 or d + dists[min_node] < dists[nxt]:
                    dists[nxt] = d + dists[min_node]
                    counts[nxt] = counts[min_node]
                elif d + dists[min_node] == dists[nxt]:
                    counts[nxt] = (counts[min_node] + counts[nxt]) % 1_000_000_007
            min_node = -1
            for i in range(n):
                if (not dones[i]) and dists[i] != -1 and (min_node == -1 or dists[i] < dists[min_node]):
                    min_node = i
            dones[min_node] = True
        return counts[-1]

            