class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while additionalTank > 0 and mainTank >= 5:
            t = mainTank // 5
            ans += t * 5
            mainTank -= t * 5
            t = min(t, additionalTank)
            additionalTank -= t
            mainTank += t
        ans += mainTank
        return 10 * ans
