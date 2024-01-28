class Solution:
    def canMeasureWater(self, j1: int, j2: int, cap: int) -> bool:
        if j1 + j2 < cap:
            return False
        if j1 == 0 or j2 == 0:
            return cap == 0 or cap == j1 + j2
        def gcd(a, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        return cap % (gcd(j1, j2)) == 0