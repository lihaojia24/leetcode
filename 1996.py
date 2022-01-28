from typing import List

class Solution:
  def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
    properties.sort(key = lambda x : (-x[0], x[1]))
    ans = 0
    maxDef = 0
    for _, _def in properties:
      if _def < maxDef:
        ans += 1
      else:
        maxDef = _def
    return ans

class Solution:
  def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
    properties.sort(key = lambda x : (x[0], -x[1]))
    ans = 0
    q = []
    for _, _def in properties:
      while q and q[-1] < _def:
        q.pop()
        ans += 1
      q.append(_def)
    return ans
