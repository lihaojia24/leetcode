from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for times in citations:
            if times > n:
                cnt[n] += 1
            else:
                cnt[times] += 1
        for i in range(n, 0, -1):
            if cnt[i] >= i:
                return i
            cnt[i-1] += cnt[i]
        return 0
        