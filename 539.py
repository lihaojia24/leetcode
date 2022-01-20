from typing import List

class Solution:
  def findMinDifference(self, timePoints: List[str]) -> int:
    def getMinutes(t: str) -> int:
      return ((ord(t[0]) - ord('0')) * 10 + ord(t[1]) - ord('0')) * 60 + (ord(t[3]) - ord('0')) * 10 + ord(t[4]) - ord('0')
    
    res = [0] * 1440
    n = len(timePoints)
    if n > 1440:
      return 0

    for timePoint in timePoints:
      res[getMinutes(timePoint)] += 1
    
    preTime = -1
    start = -1
    ans = 1500
    for i in range(1440):
      if res[i] > 1:
        return 0
      if res[i] == 1:
        if preTime == -1:
          preTime = i
          start = i
        else:
          gap = i - preTime
          preTime = i
          ans = gap if gap < ans else ans
    gap = start - preTime + 1440
    ans = gap if gap < ans else ans
    return ans


