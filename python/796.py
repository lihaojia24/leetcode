def getNext(s: str) -> str:
  n = len(s)
  nx = [-1] * n
  i, j = 0, -1
  while i < n - 1:
    if j == -1 or s[j] == s[i]:
      i, j = i + 1, j + 1
      nx[i] = j
    else:
      j = nx[j]
  return nx

class KMP():
  def __init__(self, s: str):
    self.s = s
    self.n = len(s)
    self.nx = getNext(s)
  
  def isMatch(self, s: str):
    i, j = 0, 0
    while i < len(s):
      if s[i] == self.s[j]:
        if j == self.n - 1: return True
        j += 1
        i += 1
      else:
        nx = self.nx[j]
        if nx == -1:
          j = 0
          i += 1
        else:
          j = nx
    return False

class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    if len(s) != len(goal): return False
    k = KMP(goal)
    return k.isMatch(s + s)


# k = KMP('cda')
# print(k.isMatch('caddcxda'))

so = Solution()
s = 'abcde'
goal = 'abced'
print(so.rotateString(s, goal))

        

    