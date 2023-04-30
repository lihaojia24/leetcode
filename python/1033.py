from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        (x, y, z) = sorted(a, b, c)
        mi, mx = 0
        if z - x > 2:
            mi = 1 if y - x < 3 or z - y < 3 else 2
            mx = z - x - 2
        return [mi, mx]