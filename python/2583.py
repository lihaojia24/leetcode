class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        times = time // (n - 1)
        res = time % (n - 1)
        if times % 2:
            return n - res
        return res + 1