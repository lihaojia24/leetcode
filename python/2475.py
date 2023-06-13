from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] != nums[j]:
                    for z in range(j+1, n):
                        if nums[z] != nums[i] and nums[z] != nums[j]:
                            ans += 1
        return ans