from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        v = [False] * n
        def dfs(n: int) -> int:
            ans = 0
            q = [n]
            while q:
                x = q.pop()
                if not v[x]:
                    ans += 1
                    v[x] = True
                    for y in g[x]:
                        q.append(y)
            return ans
        ans = 0
        total = 0
        for i in range(n):
            s = dfs(i)
            ans += s * total
            total += s
        return ans
            

s = Solution()
n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
print(s.countPairs(n,edges))
        
