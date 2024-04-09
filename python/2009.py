from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        s_nums = sorted(set(nums))
        ans = left = 0
        for right, num in enumerate(s_nums):
            while s_nums[left] < num - n + 1:
                left += 1
            ans = max(ans, right - left + 1)
        return n - ans