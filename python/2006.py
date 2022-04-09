from typing import Counter, List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
      res = 0
      cnt = Counter(nums)
      for key in cnt:
        count = cnt[key]
        res += count * cnt[key + k] 
        res += count * cnt[key - k]
        cnt[key] = 0
      return res


nums = [3,2,1,5,4]
k = 2
solu = Solution()
res = solu.countKDifference(nums, k)
print(res)