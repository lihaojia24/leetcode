from heapq import heapify, heapreplace
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = - (nums[i] << 20 )
        heapify(nums)
        ans = 0
        half = sum(nums) >> 1
        while half < 0:
            half -= nums[0] >> 1
            heapreplace(nums, nums[0] >> 1)
            ans += 1
        return ans