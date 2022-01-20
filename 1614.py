class Solution:
  def maxDepth(self, s: str) -> int:
    res = 0
    tmp = 0
    for ch in s:
      if ch == '(':
        tmp += 1
        res = tmp if tmp > res else res
      elif ch == ')':
        tmp -= 1
    return res