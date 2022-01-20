from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = 0
        for num in nums:
            xorsum ^= num
        
        lsb = xorsum & (-xorsum)

        ans1, ans2 = 0, 0
        for num in nums:
            if num & lsb:
                ans1 ^= num
            else:
                ans2 ^= num

        return [ans1, ans2]