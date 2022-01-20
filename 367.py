class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            pow = mid * mid
            if pow == num:
                return True
            elif pow < num:
                left = mid + 1
            else:
                right = mid - 1
        return False