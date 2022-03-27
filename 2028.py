from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
      m = len(rolls)
      gap = (m + n) * mean - sum(rolls) - n
      if gap < 0 or gap > 5 * n: return []
      num5 = gap // 5
      numRes = gap % 5
      num1 = n - num5 - 1
      ans = [6] * num5
      if num5 < n: ans.append(numRes + 1)
      if num1 > 0: ans.extend([1] * num1)
      return ans
      
s = Solution()
rolls = [1,2,3,4]
mean = 6
n = 4
print(s.missingRolls(rolls, mean, n))
