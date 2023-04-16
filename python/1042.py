from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for b, e in paths:
            g[b - 1].append(e - 1)
            g[e - 1].append(b - 1)
        res = [0] * n
        for i, links in enumerate(g):
            mask = 1
            for link in links:
                mask |= 1 << res[link]
            mask = ~mask
            res[i] = (mask & -mask).bit_length() - 1

        return res