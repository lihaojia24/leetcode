class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        t = num
        while t:
            ans += 1 if (num % (t % 10)) == 0 else 0
            t //= 10
        return ans