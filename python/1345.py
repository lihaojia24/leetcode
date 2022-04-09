from collections import deque
from typing import DefaultDict, List

class Solution:
  def minJumps(self, arr: List[int]) -> int:
    n = len(arr)
    sameKey = DefaultDict(list)
    for i, num in enumerate(arr):
      sameKey[num].append(i)
    q = deque()
    q.append([0, 0])
    visited = {0}
    while q:
      index, step = q.popleft()
      if index == n - 1:
        return step
      step += 1
      for i in sameKey[arr[index]]:
        if i not in visited:
          q.append([i, step])
          visited.add(i)
      del sameKey[arr[index]]
      if index < n - 1 and (index + 1) not in visited:
        q.append([index + 1, step])
        visited.add(index + 1)
      if index > 0 and (index - 1) not in visited:
        q.append([index - 1, step])
        visited.add(index - 1)
    return -1
      
          
solu = Solution()
arr = [100,-23,-23,404,100,23,23,23,3,404]
print(solu.minJumps(arr))


