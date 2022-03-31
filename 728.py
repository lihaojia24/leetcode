from typing import List

class Solution:
  def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    def isDividingNumber(num):
      x = num
      while x:
        tmp = x % 10
        if tmp == 0 or num % tmp:
          return False
        x = x // 10
      return True

    ans = []
    for num in range(left, right + 1):
      if isDividingNumber(num): ans.append(num)
    return ans

s = Solution()
left = 1
right = 22
print(s.selfDividingNumbers(left, right))