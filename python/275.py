from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations[-1] == 0: return 0
        n = len(citations)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2 + 1
            x = n - mid
            t = citations[mid]
            if t < x:
                r = mid - 1
            else:
                l = mid
        return min(n - l, citations[l])
