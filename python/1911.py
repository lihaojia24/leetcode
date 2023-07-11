from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        p, r = 0, 0
        nP, nR = p, r
        for num in nums:
            nP = max(r - num, p)
            nR = max(p + num, r)
            p, r = nP, nR
        return max(p, r)