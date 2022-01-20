#264ms 166MB
from typing import List
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return  max((value + cnt[key + 1] for key, value in cnt.items() if key + 1 in cnt), default = 0)

#300ms 162MB
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans, begin = 0, 0
        for end in range(n):
            if end + 1 < n and nums[end + 1] == nums[end]:
                continue
            while nums[end] - nums[begin] > 1:
                begin += 1
            if nums[end] - nums[begin] == 1:
                ans = max(ans, end - begin + 1)
        return ans

#308ms 162MB
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans, begin = 0, 0
        for end in range(n):
            # if end + 1 < n and nums[end + 1] == nums[end]:
                # continue
            while nums[end] - nums[begin] > 1:
                begin += 1
            if nums[end] - nums[begin] == 1:
                ans = max(ans, end - begin + 1)
        return ans