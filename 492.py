from math import sqrt
from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(sqrt(area))
        while area % w:
            w -= 1
        return area // w, w


solu = Solution()
print(solu.constructRectangle(4))