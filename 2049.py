from enum import EnumMeta
from typing import List

# class Solution:
#   def countHighestScoreNodes(self, parents: List[int]) -> int:
#     n = len(parents)
#     nodeCnt = [1] * n
#     ans = [1] * n
#     for parent in parents:
#       while parent != -1:
#         nodeCnt[parent] += 1
#         parent = parents[parent]
#     for i in range(n):
#       parent = parents[i]
#       if parent != -1:
#         ans[i] *= n - nodeCnt[i]
#         ans[parent] *= nodeCnt[i]
#     cnt, m = 0, 0
#     for score in ans:
#       if score > m:
#         m = score
#         cnt = 1
#       elif score == m:
#         cnt += 1
#     return cnt

class Solution:
  def countHighestScoreNodes(self, parents: List[int]) -> int:
    n = len(parents)
    childrens = [[] for _ in range(n)]
    scores = [1] * n
    for i, parent in enumerate(parents):
      if parent != -1:
        childrens[parent].append(i)
    # print(childrens)
    def dfs(node: int) -> int:
      weight, score = 1, 1
      for child in childrens[node]:
        childWeight = dfs(child)
        weight += childWeight
        score *= childWeight
      score *= n - weight if (n - weight) else 1
      scores[node] = score
      return weight
    dfs(0)
    cnt, m = 0, 0
    for score in scores:
      if score > m:
        m = score
        cnt = 1
      elif score == m:
        cnt += 1
    return cnt


    

s = Solution()
parents = [-1,2,0,2,0]
print(s.countHighestScoreNodes(parents))