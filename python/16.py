from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target): res = s
                if res - target == 0: return res
                if s > target: r -= 1
                else: l += 1
        return res
    
s = Solution()
nums = [-1,2,1,-4]
target = 1
print(s.threeSumClosest(nums, target))