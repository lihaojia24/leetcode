class Solution:
  def hasAlternatingBits(self, n: int) -> bool:
    flag = 1 & n
    n >>= 1
    while n:
      if 1 & n == flag: return False
      else: 
        flag = 1 & n
        n >>= 1
    return True

s = Solution()
print(s.hasAlternatingBits(11))