from typing import DefaultDict, List

class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    vote = [0] * (n + 1)
    for i,o in trust:
      vote[i] = -1
      if vote[o] != -1:
        vote[o] += 1
    for i in range(1, n+1):
      if vote[i] == n-1:
        return i
    return -1

