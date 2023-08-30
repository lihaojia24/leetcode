from collections import deque
from typing import List

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        bound = max(x + b, max(forbidden) + a + b)
        sForbidden = set(forbidden)
        q = deque([(0, 1)])
        vis = set()
        ans = 0
        while q:
            print(q)
            for _ in range(len(q)):
                pos, dir = q.popleft()
                if pos == x: return ans
                if pos < 0 or pos > bound: continue
                if pos in sForbidden: continue
                if (pos, dir) in vis: continue
                q.append((pos + a, 1))
                if dir == 1: q.append((pos - b, 0))
                vis.add((pos, dir))
            ans += 1
        return -1
    
s = Solution()
f = [18,13,3,9,8,14]
a = 3
b = 8
x = 6
x = s.minimumJumps(f,a,b,x)
print(x)