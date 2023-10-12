from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        ans = 0
        while i <= j:
            if i == j:
                ans += nums[i]
            else:
                a, b = nums[i], nums[j]
                while b > 0:
                    a *= 10
                    b //= 10
                ans += (a + nums[j])
            i += 1
            j -= 1
        return ans