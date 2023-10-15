from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31):
            total = sum((num >> i) & 1 for num in nums)
            ans |= (total % 3) << i
        total = sum((num >> 31) & 1 for num in nums)
        if total % 3:
            total = 1 & 0xffffffff
        ans |= total
        return ans