from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mn, mx = nums[0], nums[0]
        mni, mxi = nums[0], nums[0]
        s = nums[0]
        for num in nums[1:]:
            # mx
            mxi = max(mxi + num, num)
            mx = max(mx, mxi)
            #  mn
            mni = min(mni + num, num)
            mn = min(mn, mni)
            # s
            s += num
        return mx if mx < 0 else max(mx, s - mn)
    
s = Solution()
nums = [-3,-2,-3]
print(s.maxSubarraySumCircular(nums))