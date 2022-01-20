from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        kind = len(set(candyType))
        num = len(candyType) // 2
        return min(kind, num)
