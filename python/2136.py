from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = days = 0
        for p, g in sorted(zip(plantTime, growTime), key=lambda x: -1 * x[1]):
            days += p
            ans = max(ans, days + g)
        return ans