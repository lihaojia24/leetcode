from functools import reduce
from operator import or_
from typing import List

# 枚举
class Solution:
  def countMaxOrSubsets(self, nums: List[int]) -> int:
    maxAns, cnt = 0, 0
    for mask in range(1 << len(nums)):
      # ans = reduce(or_, (num for i, num in enumerate(nums) if (mask & 1 << i)), 0)
      ans = reduce(or_, (num for i, num in enumerate(nums) if (mask >> i) & 1), 0)
      if ans > maxAns:
        maxAns = ans
        cnt = 1
      elif ans == maxAns:
        cnt += 1
    return cnt

# 回溯
class Solution:
  def countMaxOrSubsets(self, nums: List[int]) -> int:
    maxAns, cnt = 0, 0
    def dfs(index, cur):
      # nonlocal maxAns, cnt
      if index == len(nums):
        if cur > maxAns:
          maxAns = cur
          cnt = 1
        elif cur == maxAns:
          cnt += 1
        return
      dfs(index + 1, cur)
      dfs(index + 1, cur | nums[index])
    dfs(0, 0)
    return cnt
