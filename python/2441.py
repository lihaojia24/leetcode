from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = [0] * 2001
        ans = -1
        for num in nums:
            res[num] = 1
            if res[-1 * num] == 1:
                ans = max(ans, num, -1 * num)
        return ans
