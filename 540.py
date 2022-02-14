from functools import reduce
from typing import List

class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)

nums = [1,2,3,2,3,1,55]
solu = Solution()
print(solu.singleNonDuplicate(nums))