from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque([s])
        vis = {s}
        ans = s
        while q:
            s = q.popleft()
            if s < ans:
                ans = s
            n1 = ''.join([str((int(ch) + a) % 10) if i % 2 else ch for i, ch in enumerate(s)])
            n2 = s[b:]+s[:b]
            for n in (n1,n2):
                if n not in vis:
                    vis.add(n)
                    q.append(n)
        return ans