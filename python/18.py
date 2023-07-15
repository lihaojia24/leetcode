from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for a in range(n-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n-2):
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue
                c, d = b + 1, n -1
                while c < d:
                    if nums[a] + nums[b] == target - nums[c] - nums[d]:
                        print(a,b,c,d)
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                    if nums[a] + nums[b] <= target - nums[c] - nums[d]:
                        while c < d and nums[c] == nums[c+1]:
                            c += 1
                        c += 1
                    else:
                        while d > c and nums[d] == nums[d-1]: 
                            d -= 1
                        d -= 1
        return ans
    
s = Solution()
nums = [2,2,2,2,2]
target = 8
print(s.fourSum(nums,target))