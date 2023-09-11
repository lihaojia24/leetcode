from typing import List
import heapq

class Solution:
  def scheduleCourse(self, courses: List[List[int]]) -> int:
    courses.sort(key = lambda x: x[1])
    q = []
    spendtime = 0
    for duration, deadline in courses:
      if spendtime + duration <= deadline:
        spendtime += duration
        heapq.heappush(q, -duration)
      elif q and -q[0] > duration:
        spendtime += heapq.heappop(q)
        spendtime += duration
        heapq.heappush(q, -duration)
    return len(q)