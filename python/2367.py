from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        m = [0] * 201
        ans = 0
        for num in nums:
            m[num] = 1
        for num in nums:
            if m[num+diff] == 1 and m[num+2*diff] == 1:
                ans += 1
        return ans