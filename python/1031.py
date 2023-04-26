from itertools import accumulate
from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        s = list(accumulate(nums, initial=0))
        ans = 0
        def f(firstLen: int, secondLen: int) -> None:
            nonlocal ans
            maxSumA = 0
            maxSumB = 0
            for i in range(firstLen + secondLen, len(s)):
                maxSumB = max(maxSumB, s[i-firstLen] - s[i-firstLen-secondLen])
                maxSumA = max(maxSumA, s[i-secondLen] - s[i-firstLen-secondLen])
                ans = max(ans, maxSumB + s[i] - s[i-firstLen])
                ans = max(ans, maxSumA + s[i] - s[i-secondLen])
        f(firstLen, secondLen)
        # f(secondLen, firstLen)
        return ans