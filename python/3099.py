class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        r = x
        s = 0
        while r > 0:
            s += r % 10
            r //= 10
        return s if x % s == 0 else -1