from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx, mn = 0, 0
        ans = 0
        for num in nums:
            mx = max(0, mx+num)
            mn = min(0, mn+num)
            print(mx, mn)
            ans = max(mx, -mn, ans)
        return ans
    
nums = [1,-3,2,3,-4]
s = Solution()
s.maxAbsoluteSum(nums)