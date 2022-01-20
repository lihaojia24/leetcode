from typing import List
import heapq

class Solution:
  def scheduleCourse(self, courses: List[List[int]]) -> int:
    courses.sort(key=lambda x:x[1])
    q = list()
    totalTime = 0

    for duration, deadline in courses:
      if totalTime + duration <= deadline:
        totalTime += duration
        heapq.heappush(q, -1 * duration)
      elif q and -1 * q[0] > duration:
        totalTime += duration + q[0]
        heapq.heappop(q)
        heapq.heappush(q, -1 * duration)
    
    return len(q)
