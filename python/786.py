from typing import List

# 二分查找 + 双指针
# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#       n = len(arr)
#       left = 0.0
#       right = 1.0

#       while left < right:
#         mid = (left + right) / 2.0
#         i = -1
#         count = 0
#         x = 0
#         y = 1
#         for j in range(1, n):
#           while arr[i+1]/arr[j] < mid:
#             i += 1
#             if arr[i] * y > arr[j] * x:
#               x, y = arr[i], arr[j]
#           count += i + 1
        
#         if k == count:
#           return [x, y]
#         elif k < count:
#           right = mid
#         else:
#           left = mid
#       return None

# 自定义排序
# from functools import cmp_to_key
# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#       def cmp(x,y):
#         return 1 if x[0] * y[1] > x[1] * y[0] else -1

#       n = len(arr)

#       frac = list()
#       for i in range(n-1):
#         for j in range(i+1,n):
#           frac.append([arr[i], arr[j]])
          
#       frac.sort(key=cmp_to_key(cmp))

#       return frac[k-1]

# 优先队列

class Frac:
  def __init__(self, idx, idy, x, y) -> None:
    self.idx = idx
    self.idy = idy
    self.x = x
    self.y = y
  
  def __lt__(self, other) -> bool:
    return self.x * other.y < self.y * other.x


import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
      n = len(arr)
      q = [Frac(i, n-1, arr[i], arr[n-1]) for i in range(n-1)]
      heapq.heapify(q)
      for _ in range(k-1):
        frac = heapq.heappop(q)
        i, j = frac.idx, frac.idy
        if j - 1 > i:
          heapq.heappush(q, Frac(i, j-1, arr[i], arr[j-1]))
      return [q[0].x, q[0].y]
