

import heapq
from typing import List

# 1
class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    m, n = len(nums1), len(nums2)
    q = [(nums1[i] + nums2[0], i, 0) for i in range(min(m, k))]
    ans = []
    while q and len(ans) < k:
      _, i, j = heapq.heappop(q)
      ans.append((nums1[i], nums2[j]))
      if j < n - 1:
        heapq.heappush(q, (nums1[i]+ nums2[j + 1], i, j + 1))
    return ans

# 1
class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    