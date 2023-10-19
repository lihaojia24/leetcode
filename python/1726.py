from collections import defaultdict
from typing import List

class Solution:   
    def tupleSameProduct(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                m[nums[i] * nums[j]] += 1
        return sum(x * (x - 1) // 2 for x in m.values()) << 3

s = Solution()
nums = [1,2,4,5,10]
print(s.tupleSameProduct(nums))
