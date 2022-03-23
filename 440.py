import pdb

class Solution:
  def findKthNumber(self, n: int, k: int) -> int:
    ans = 1
    while k > 1:
      cnt = self.getCnt(ans, n)
      if cnt < k:
        ans += 1
        k -= cnt
      else:
        ans *= 10
        k -= 1 
    return ans
  
  def getCnt(self, prefix: int, limit: int) -> int:
    # pdb.set_trace()
    prefixStr, limitStr = str(prefix), str(limit)
    nPrefix, nLimit = len(prefixStr), len(limitStr)
    k = nLimit - nPrefix
    ans = 0
    for i in range(k): ans += 10 ** i
    preValue = int(limitStr[:nPrefix])
    print(prefix, preValue)
    if preValue > prefix: ans += 10 ** k
    elif preValue == prefix: ans += (limit - prefix * (10 ** k) + 1)
    return ans

s = Solution()
print(s.findKthNumber(2, 2))
