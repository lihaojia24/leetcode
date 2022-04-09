from typing import List

class Solution:
  def calPoints(self, ops: List[str]) -> int:
    ans = []
    for op in ops:
      if op == '+':
        ans.append(ans[-2] + ans[-1])
      elif op == 'D':
        ans.append(ans[-1] * 2)
      elif op == 'C':
        ans.pop()
      else:
        ans.append(int(op))
    print(ans)
    return sum(ans)

s = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print(s.calPoints(ops))