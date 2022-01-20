class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend > INT_MIN:
                return -dividend
            return INT_MAX
        
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor

        def div(dividend: int, divisor: int) -> int:
            if dividend < divisor:
                return 0
            ans = 1
            tmpDivisor = divisor
            while tmpDivisor + tmpDivisor <= dividend:
                ans += ans
                tmpDivisor += tmpDivisor
            return ans + div(dividend - tmpDivisor, divisor)

        ans = div(dividend, divisor)

        if sign > 0:
            return ans
        else:
            return -ans

solu = Solution()
dividend = 8
divisor = 3
print(solu.divide(dividend, divisor))

        
