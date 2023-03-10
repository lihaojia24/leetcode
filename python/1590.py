from itertools import accumulate
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        acc = list(accumulate(nums, initial=0))
        res = acc[-1] % p
        if res == 0: return 0
        ans = n = len(nums)
        last = {}
        for i, num in enumerate(acc):
            last[num % p] = i
            j = last.get((num - res) % p, -n)
            ans = min(ans, i-j)
        return ans if ans < n else -1