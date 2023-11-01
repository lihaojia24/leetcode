from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        deg = [0] * n
        max_depth = [1] * n
        for f in favorite:
            deg[f] += 1
        q = []
        for i, d in enumerate(deg):
            if d == 0: q.append(i)
        while q:
            node = q.pop()
            nxt = favorite[node]
            deg[nxt] -= 1 
            max_depth[nxt] = max(max_depth[node] + 1, max_depth[nxt])
            if deg[nxt] == 0: q.append(nxt)
        max_ring_size = 0
        max_line_size = 0
        for i, d in enumerate(deg):
            if d != 0:
                deg[i] = 0
                nxt = favorite[i]
                ring_size = 1
                while nxt != i:
                    ring_size += 1
                    deg[nxt] = 0
                    nxt = favorite[nxt]
                if ring_size == 2:
                    max_line_size += max_depth[i] + max_depth[favorite[i]] 
                else:
                    max_ring_size = max(max_ring_size, ring_size)
                print(max_ring_size, max_line_size, i, favorite[i])
        return max(max_ring_size, max_line_size)