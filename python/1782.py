from collections import Counter
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        deg = [0] * (n + 1)
        cnt_e = dict()
        for x, y in edges:
            if y < x: x, y = y, x
            deg[x] += 1
            deg[y] += 1
            cnt_e[(x,y)] = cnt_e.get((x,y), 0) + 1

        cnt_deg = Counter(deg[1:])

        cnts = [0] * (max(deg) * 2 + 2)
        for deg1, c1 in cnt_deg.items():
            for deg2, c2 in cnt_deg.items():
                if deg1 < deg2:
                    cnts[deg1 + deg2] += c1 * c2
                if deg1 == deg2:
                    cnts[deg1 + deg2] += c1 * (c1 - 1) // 2

        for (x, y), c in cnt_e.items():
            s = deg[x] + deg[y]
            cnts[s] -= 1
            cnts[s - c] += 1
        
        for i in range(len(cnts) - 1, 0, -1):
            cnts[i-1] += cnts[i]
        
        ans = []
        for q in queries:
            ans.append(cnts[min(q + 1, len(cnts) - 1)])
        return ans

        