from functools import reduce

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows < 2: return s
    ans = ['' for _ in range(numRows)]
    i, flag = 0, -1
    for c in s:
      ans[i] += c
      if i == 0 or i == numRows - 1: flag = -flag
      i += flag
    return ''.join(ans)


# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
s = "PAYPALISHIRING"
numRows = 3
solu = Solution()
print(solu.convert(s, numRows))