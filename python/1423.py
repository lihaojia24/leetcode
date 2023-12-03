from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        points = [0] * (k + 1)
        l, r = 0, 0
        n = len(cardPoints)
        for i in range(k):
            l += cardPoints[i]
            r += cardPoints[-1-i]
            points[i+1] += l
            points[-2-i] += r
        return max(points)