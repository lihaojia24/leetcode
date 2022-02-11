from typing import List

class Solution:
  def minimumDifference(self, nums: List[int], k: int) -> int:
    MAX_INT = 2**31 - 1
    ans = MAX_INT
    nums.sort()
    for i in range(k - 1, len(nums)):
      gap = nums[i] - nums[i - k + 1]
      ans = ans if ans < gap else gap

    return ans

nums = [9,4,1,7]
k = 2
solu = Solution()
ans = solu.minimumDifference(nums, k)

print(ans)