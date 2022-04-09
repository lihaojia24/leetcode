

class Solution:
  def convertToBase7(self, num: int) -> str:
    UNIT = 7
    ans = []
    flag = False
    if num < 0:
      flag = True
      num = -num  
    while num:
      ans.append(str(num % 7))
      num //= 7
    ans = ('-' if flag else '') + ''.join(ans[::-1])
    return ans if ans else '0'
    
s = Solution()
print(s.convertToBase7(-7))