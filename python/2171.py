from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans.sort()
        preSum = [0] * n
        preSum[0] = beans[0]
        # for i, bean in enumerate(beans[1:]):
        #     preSum[i] += preSum[i-1] + bean
        # res = preSum[-1]
        s = sum(beans)
        res = s
        for i, bean in enumerate(beans):
            x = s - bean * (n - i)
            res = min(res, x)
        return res
        
