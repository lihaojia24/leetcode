from typing import List

class Solution:
  def maximumDifference(self, nums: List[int]) -> int:
    minimal = nums[0]
    ans = -1
    for num in nums[1:]:
      gap = num - minimal
      ans = gap if gap > ans and gap > 0 else ans
      minimal = num if num < minimal else minimal
    return ans