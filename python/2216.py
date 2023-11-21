from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                i += 2
            else:
                i += 1
                ans += 1
        if (len(nums) - ans) % 2 == 1:
            ans += 1
        return ans