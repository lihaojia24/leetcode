from cmath import inf
from typing import List

class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        mx = max(vat)
        if mx == 0: return 0
        ans = 10 ** 4 + 1
        for x in range(1, mx + 1):
            tmp = x
            for b, v in zip(bucket, vat):
                tmp += max(0, (v + x - 1) // x - b)
            ans = min(ans, tmp)
        return ans
