from typing import List

class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    minN, maxN = nums[0], (1 << 31) - 1
    for num in nums[1:]:
      if num > maxN:
        return True
      if num <= minN:
        minN = num
      else:
        maxN = num
    return False