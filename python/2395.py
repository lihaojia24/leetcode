from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        m = {}
        tmp = 0
        for i in range(len(nums)-1):
            tmp = nums[i] + nums[i+1]
            if tmp in m:
                return True
            m[tmp] = 1
        return False