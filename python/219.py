from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    win = set()
    for i in range(len(nums)):
      if nums[i] in win:
        return True
      win.add(nums[i])
      if i >= k:
        win.remove(nums[i - k])  
      
    return False


