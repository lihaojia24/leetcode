from collections import deque
from math import inf
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        # xj + yj + (yi - xi)
        # xi >= xj - k
        # q (xi, yi - xi)
        ans = -inf
        for x, y in points:
            while q and q[0][0] < x - k:
                q.popleft()
            if q:
                ans = max(ans, x + y + q[0][1])
            while q and q[-1][1] < y - x:
                q.pop()
            q.append((x, y - x))
        return ans