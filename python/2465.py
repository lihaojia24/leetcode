from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        ansSet = set()
        l, r = 0, len(nums)-1
        while l < r:
            ansSet.add((nums[l] + nums[r]) / 2)
            l+=1
            r-=1
        return len(ansSet)