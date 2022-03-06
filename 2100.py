from operator import le
from turtle import left, right
from typing import List

class Solution:
  def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
    n = len(security)
    left, right = [False] * n, [False] * n
    if time == 0:
      left[0], right[-1] = True, True
    count = 0
    for i in range(1, n):
      if security[i] <= security[i - 1]: count += 1
      else: count = 0
      if count >= time: left[i] = True
    count = 0
    for i in range(n - 2, -1, -1):
      if security[i] <= security[i + 1]: count += 1
      else: count = 0
      if count >= time: right[i] = True
    ans = []
    for i in range(n):
      if left[i] and right[i]: ans.append(i)
    return ans

s = Solution()
security = [1,2,3,4,5,6]
time = 2
print(s.goodDaysToRobBank(security, time))