from typing import List


class Solution:
  def dominantIndex(self, nums: List[int]) -> int:
    ans = -1
    second = -1
    idx = 0
    for index, num in enumerate(nums):
      if num > ans:
        ans, second = num, ans
        idx = index
      elif num > second:
        second = num
    return idx if ans >= 2 * second else -1