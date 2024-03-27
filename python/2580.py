from typing import List

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 1_000_000_007
        ranges.sort(key=lambda x: x[0])
        ans = 1
        max_r = -1
        for l, r in ranges:
            if l > max_r:
                ans = (ans * 2) % MOD
            max_r = max(max_r, r)
        return ans