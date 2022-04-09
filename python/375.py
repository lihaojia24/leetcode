class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = min([k + max(dp[i][k-1], dp[k+1][j]) for k in range(i, j+1)])
        return dp[1][n]

solu = Solution()
for i in range(1, 10):
    print(solu.getMoneyAmount(i))