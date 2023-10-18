import heapq
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = [-num for num in nums]
        heapq.heapify(h)
        ans = 0
        for _ in range(k):
            num = -heapq.heappop(h)
            ans += num
            heapq.heappush(-(num + 2) // 3)
        return ans

