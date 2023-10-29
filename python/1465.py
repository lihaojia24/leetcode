from itertools import pairwise
from typing import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        h_cuts = [0] + sorted(horizontalCuts) + [h]
        v_cuts = [0] + sorted(verticalCuts) + [w]
        h_max = max(y - x for x, y in pairwise(h_cuts))
        v_max = max(y - x for x, y in pairwise(v_cuts))
        return h_max * v_max % MOD