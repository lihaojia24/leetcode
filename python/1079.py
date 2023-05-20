from collections import Counter
from math import comb


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnts = Counter(tiles).values()
        n, m = len(cnts), len(tiles)
        ans = [[0] * (m + 1)  for _ in range(n + 1)]
        ans[0][0] = 1
        for i, cnt in enumerate(cnts, 1):
            for j in range(m + 1):
                for k in range(min(cnt, j) + 1):
                    ans[i][j] += ans[i-1][j-k] * comb(j, k)
        return sum(ans[n][:])