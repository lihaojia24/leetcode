import math
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        steps = []
        for d, s in zip(dist,speed):
            steps.append(math.ceil(d/s))
        steps.sort()
        print(steps)
        ans = 0
        for i, s in enumerate(steps):
            if s <= i:
                return ans
            ans += 1
        return ans
    
dist = [3,2,4]
speed = [5,3,2]
s = Solution()
v = s.eliminateMaximum(dist, speed)
print(v)