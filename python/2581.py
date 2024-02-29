from typing import List

class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int: 
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        guess_set = {(x, y) for x, y in guesses}
        ans = 0
        cnt0 = 0
        def dfs(x: int, fa: int) -> None:
            nonlocal cnt0
            for y in g[x]:
                if y != fa:
                    cnt0 += (x, y) in guess_set
                    dfs(y, x)
        dfs(0, -1)
        def reroot(x: int, fa: int, cnt: int) -> None:
            nonlocal ans
            if (fa, x) in guess_set: cnt -= 1
            if (x, fa) in guess_set: cnt += 1
            if cnt >= k : ans += 1
            for y in g[x]:
                if y != fa:
                    reroot(y, x, cnt)
        reroot(0, -1, cnt0)
        return ans


