from typing import List

class Solution:
  def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
    ans = 0
    for mask in range(1 << len(requests)):
      cnt = mask.bit_count()
      if cnt <= ans:
        continue
      delta = [0] * n
      for i, (x, y) in enumerate(requests):
        if mask & (1 << i):
          delta[x] -= 1
          delta[y] += 1
      if all( x == 0 for x in delta):
        ans = cnt
    return ans


n = 5
requests = [[2,0],[0,4],[3,1],[2,4],[1,3],[4,2],[4,3],[0,1]]
s = Solution()
print(s.maximumRequests(n, requests))