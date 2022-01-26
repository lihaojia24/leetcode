from collections import defaultdict
from typing import Counter, List


class DetectSquares:

    def __init__(self):
      self.points = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
      x, y = point
      self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
      x, y = point
      ans = 0
      if x not in self.points:
        return ans
      xPoints = self.points[x]

      for otherX, otherXPoints in self.points.items():
        if otherX != x:
          d = otherX - x
          point1 = otherXPoints[y]
          point2 = xPoints[y + d]
          point3 = otherXPoints[y + d]
          point22 = xPoints[y - d]
          point33 = otherXPoints[y - d]
          ans += point1 * point2 * point3
          ans += point1 * point22 * point33
      return ans