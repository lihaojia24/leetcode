from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        tmp = -1
        while i + 1 < len(nums):
            if tmp < 0:
                tmp = nums[i] + nums[i+1]
                ans += 1
            elif tmp == nums[i] + nums[i+1]:
                ans += 1
            else:
                break
            i += 2
        return ans