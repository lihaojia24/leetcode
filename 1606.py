from heapq import heappop, heappush
from typing import List

class Solution:
  def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
    avaliable = list(range(k))
    busy = []
    request = [0] * k
    for i, (start, t) in enumerate(zip(arrival, load)):
      while busy and busy[0][0] <= start:
        _, id = heappop(busy)
        heappush(avaliable, i + (id - i) % k)
      if avaliable:
        id = heappop(avaliable) % k
        request[id] += 1
        heappush(busy, (start + t, id))
    maxQ = max(request)
    return [i for i in range(k) if request[i] == maxQ]