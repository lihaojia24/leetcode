from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if(nums[i]>0):
                return ans
            if(i>0 and nums[i]==nums[i-1]):
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0: ans.append([nums[i], nums[l], nums[r]])
                if s > 0: r -= 1
                else: l += 1
        return ans
    
s = Solution()
nums = [0,0,0,0]
print(s.threeSum(nums))