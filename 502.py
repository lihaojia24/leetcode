from typing import List

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        n, index = len(profits), 0
        peers = [(capital[i], profits[i]) for i in range(n)]
        peers.sort(key = lambda x : x[0])

        hq = []
        for _ in range(k):
            while index < n and peers[index][0] <= w:
                heapq.heappush(hq, -1 * peers[index][1])
                index += 1
            if hq:
                w -= heapq.heappop(hq)
            else:
                break
        return w
