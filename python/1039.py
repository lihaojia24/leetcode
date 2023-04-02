from functools import cache
from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def df(a: int, b:int) -> int:
            if a + 1 == b : return 0
            return min(df(a,k) + df(k,b) + values[a] * values[b] * values[k] for k in range(a+1,b))
        return df(0, len(values) - 1)