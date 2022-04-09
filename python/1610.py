from typing import List
from math import atan2, pi

class Solution:
  def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
    degreeList = []
    sameCnt = 0
    for p in points:
      if p == location:
        sameCnt += 1
      else:
        degreeList.append(atan2(p[1] - location[1], p[0] - location[0]))
    degreeList.sort()
    n = len(degreeList)
    for i in range(n):
      degreeList.append(degreeList[i] + 2 * pi)
    degree = 2 * pi * angle / 360

    rightIndex = 0
    maxCnt = 0
    # 滑动窗口查找
    for i in range(n):
      while rightIndex < 2 * n and degreeList[rightIndex] <= degreeList[i] + degree:
        rightIndex += 1
      maxCnt = max(maxCnt, rightIndex - i)
    return maxCnt + sameCnt
