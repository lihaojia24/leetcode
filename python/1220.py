class Solution:
  def countVowelPermutation(self, n: int) -> int:
    dp = (1, 1, 1, 1, 1)
    for _ in range(1, n):
      dp = dp = ((dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007, (dp[1] + dp[3]) % 1000000007, dp[2], (dp[2] + dp[3]) % 1000000007)
    return sum(dp) % 1000000007