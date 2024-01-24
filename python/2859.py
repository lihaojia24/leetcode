from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def bitCount(num: int) -> int:
            cnt = 0
            while num:
                cnt+=1
                num -= num &~ (num-1)
            return cnt
        res = 0
        for i, num in enumerate(nums):
            if k == bitCount(i):
                res += num
        return res