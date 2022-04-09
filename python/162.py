from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        left, right, res = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                res = mid
                break
            elif get(mid) < get(mid + 1):
                left = mid + 1
            elif get(mid) < get(mid - 1):
                right = mid - 1
        return res