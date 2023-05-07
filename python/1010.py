from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = [0] * 60
        ans = 0
        for t in time:
            res[t%60] += 1
        # 0
        ans += res[0] * (res[0] - 1) // 2
        # 30
        ans += res[30] * (res[30] - 1) // 2
        # other
        for i in range(1,30):
            ans += res[i] * res[60 - i]
        return ans