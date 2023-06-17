class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n % 2:
            return n
        ans = 0
        while n % 2 == 0:
            ans += 1
            n /= 2
        ans += n - 1
        return ans 