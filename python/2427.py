class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if b < a:
            a, b = b, a
        t = 1
        ans = 0
        while t * t <= a:
            if a % t == 0:
                if b % t == 0:
                    print(t)
                    ans += 1
                if b % (a//t) == 0 and a//t != t:
                    print(a//t)
                    ans += 1
            t += 1
        return ans
    
s = Solution()
s.commonFactors(25, 30)