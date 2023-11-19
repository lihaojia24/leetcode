from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i = 0
        ans = 0
        while i < len(nums):
            if nums[i] <= threshold and nums[i] % 2 == 0:
                t = 1
                while i + 1 < len(nums):
                    if nums[i+1] <= threshold and (nums[i] + nums[i+1])% 2 == 1:
                        t += 1
                    else:
                        break
                    i += 1
                ans = max(ans, t)
            i += 1
        return ans