from typing import List
from heapq import *

class Solution:
  def eatenApples(self, apples: List[int], days: List[int]) -> int:
    time = 0
    ans = 0
    q = []
    while time < len(apples):
      while q and q[0][0] <= time:
        heappop(q)
      if apples[time] > 0:
        heappush(q, [time + days[time], apples[time]])
      if q:
        q[0][1] -= 1
        if q[0][1] == 0:
          heappop(q)
        ans += 1
      time += 1
    while q:
      # while q and q[0][0] < time:
      #   heappop(q)
      # if q:
      apple = heappop(q)
      if apple[0] >= time:
        num = min(apple[0] - time, apple[1])
        time += num
        ans += num
    return ans

    

# apples = [1,2,3,5,2]
# days = [3,2,1,4,2]
apples = [3,0,0,0,0,2]
days = [3,0,0,0,0,2]
solu = Solution()
print(solu.eatenApples(apples, days))