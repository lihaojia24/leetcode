from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        gap = 0
        for i in range(len(timeSeries) - 1):
            gap += max(0, timeSeries[i+1] - timeSeries[i] - duration)
        total = timeSeries[-1] - timeSeries[0] + duration
        return total - gap
