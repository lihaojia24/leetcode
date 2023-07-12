class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l, ans = 0, 0
        flag = 1
        while n > 0:
            res = n % 10
            n -= res
            n //= 10
            ans += flag * res
            flag *= -1
            l += 1
        return ans if l % 2 == 1 else ans * -1

s = Solution()
print(s.alternateDigitSum(886996))