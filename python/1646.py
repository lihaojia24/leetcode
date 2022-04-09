class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if 0 == n:
            return 0
        res = [0] * (n + 1)
        res[1] = 1
        for i in range(n+1):
            res[i] = res[i//2] + i%2 * res[i//2 + 1]
        return max(res)

n = 7
solu = Solution()
print(solu.getMaximumGenerated(n))