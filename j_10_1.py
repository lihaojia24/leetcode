class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        tmp = 0
        res = 1
        MOD = 10 ** 9 + 7
        for i in range(2, n+1):
            tmp, res = res, (res + tmp) % MOD
        return res

solu = Solution()
print(solu.fib(5))