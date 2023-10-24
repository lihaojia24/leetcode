class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if not (n<=target<=n*k):
            return 0
        MOD = 10 ** 9 + 7
        dp = [[0] * (target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, target+1):
                res = 0
                for d in range(1, k+1):
                    if j >= d:
                        res = (res + dp[i-1][j-d]) % MOD
                        # dp[i][j] += dp[i-1][j-d]
                        # dp[i][j] %= MOD
                dp[i][j] = res
        # print(dp)
        return dp[n][target]
    
s = Solution()
x = s.numRollsToTarget(2,6,7)
print(x)