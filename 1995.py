from typing import DefaultDict, List

# class Solution:
#   def countQuadruplets(self, nums: List[int]) -> int:
#     n = len(nums)
#     ans = 0
#     cnt = DefaultDict(int)
#     for b in range(n - 3, 0, -1):
#       c = b + 1
#       for d in range(b + 2, n):
#         cnt[nums[d] - nums[c]] += 1
#       for a in range(b):
#         ans += cnt[nums[a] + nums[b]]
#     return ans

class Solution:
  def countQuadruplets(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [[0] * 4 for _ in range(110)]
    dp[0][0] = 1
    ans = 0
    for i in range(1, n + 1):
      num = nums[i - 1]
      ans += dp[num][3]
      if i == n:
        break
      for j in range(109, -1, -1):
        for k in range(3, -1, -1):
          cnt = 0
          cnt += dp[j][k]
          cnt += dp[j - num][k - 1] if j - num > -1 and k - 1 > -1 else 0
          dp[j][k] = cnt
    return ans
