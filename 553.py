from enum import EnumMeta
from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
      if len(nums) == 1:
        return str(nums[0])
      if len(nums) == 2:
        return f'{nums[0]}/{nums[1]}'
      ans = f'{nums[0]}/('
      for num in nums[1:-1]:
        ans += f'{num}/'
      ans += f'{nums[-1]})'
      return ans


nums = [1000,100,10,2]
s = Solution()
print(s.optimalDivision(nums))
