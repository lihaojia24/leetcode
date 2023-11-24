from bisect import bisect_left
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        for i in range(1, len(nums)):
            res = target - nums[i]
            ans += bisect_left(nums, res, 0, i)
        return ans