from typing import List

# sliding window
class Solution:
  def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
    sum1, maxSum1, maxSum1Index = 0 ,0, 0
    sum2, maxSum2, maxSum2Index = 0 ,0, ()
    sum3, maxSum3 = 0, 0
    ans = []
    for i in range(k*2, len(nums)):
      sum1 += nums[i - k * 2]
      sum2 += nums[i - k]
      sum3 += nums[i]
      if i >= k * 3 - 1:
        if sum1 > maxSum1:
          maxSum1 = sum1
          maxSum1Index = i - k * 3 + 1
        if maxSum1 + sum2 > maxSum2:
          maxSum2 = maxSum1 + sum2
          maxSum2Index = (maxSum1Index, i - k * 2 + 1)
        if maxSum2 + sum3 > maxSum3:
          maxSum3 = maxSum2 + sum3
          ans = [*maxSum2Index, i - k + 1]
        sum1 -= nums[i - k * 3 + 1]
        sum2 -= nums[i - k * 2 + 1]
        sum3 -= nums[i - k + 1]
    return ans

# dp
class Solution:
  def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
    num = 3
    n = len(nums)
    dp = [[0] * n for i in range(num + 1)]
    dpIndex = [[] * 1 for _ in range(n)]
    for i in range(1, num + 1):
      dpIndexTmp = [[0] * i for _ in range(n)]
      for j in range(i * k - 1, n):
        if dp[i-1][j-k] + sum(nums[j-k+1:j+1]) > dp[i][j-1]:
          dp[i][j] = dp[i-1][j-k] + sum(nums[j-k+1:j+1])
          dpIndexTmp[j] = [*dpIndex[j-k], j-k+1]
        else:
          dp[i][j] = dp[i][j-1]
          dpIndexTmp[j] = dpIndexTmp[j-1]
      dpIndex = dpIndexTmp
    return dpIndex[-1]