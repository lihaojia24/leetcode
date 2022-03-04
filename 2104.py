from typing import List

class Solution:
  def subArrayRanges(self, nums: List[int]) -> int:
    ans = 0
    for i, num in enumerate(nums):
      ans += num * self.getCnt(nums, i, num)
    return ans
    
  def getCnt(self, nums, index, num) -> int:
    #As Biggest
    #L
    i, cntL = index - 1, 1
    while i > -1 and nums[i] < num:
      cntL += 1
      i -= 1
    #R
    i, cntR = index + 1, 1
    while i < len(nums) and nums[i] <= num:
      cntR += 1
      i += 1
    cntB = cntL * cntR
    #As Smallest
    #L
    i, cntL = index - 1, 1
    while i > -1 and nums[i] > num:
      cntL += 1
      i -= 1
    #R
    i, cntR = index + 1, 1
    while i < len(nums) and nums[i] >= num:
      cntR += 1
      i += 1
    cntS = cntL * cntR
    # print(cntB, cntS)
    return cntB - cntS
    
s = Solution()
nums = [4,-2,-3,4,1]
print(s.subArrayRanges(nums))



