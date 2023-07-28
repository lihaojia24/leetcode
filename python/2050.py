from collections import deque
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = [[] for _ in range(n)]
        inDeg = [0] * n
        for x, y in relations:
            g[x-1].append(y-1)
            inDeg[y-1] += 1
        q = deque(i for i, deg in enumerate(inDeg) if deg == 0)
        out = [0] * n
        while q:
            cs = q.popleft()
            out[cs] += time[cs]
            for y in g[cs]:
                out[y] = max(out[y], out[cs])
                inDeg[y] -= 1
                if inDeg[y] == 0: q.append(y)
        return max(out)
