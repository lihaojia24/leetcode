from typing import List
from math import log, ceil
from itertools import combinations
from scipy.special import comb

# math
# class Solution:
#     def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
#       state = minutesToTest // minutesToDie + 1
#       return ceil(log(buckets) / log(state))

# 
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:

      # def comb(n, m):
      #   ans = 1
      #   for i in range(n):
      #     ans *= m
      #     m -= 1
      #   return ans
      
      iteration = minutesToTest // minutesToDie
      # pigNums iteration
      dp = [[1] * (iteration + 1)] + [[1] + [0] * iteration for _ in range(buckets)]
      for i in range(1, buckets+1):
        for j in range(1, iteration + 1):
          for k in range(i + 1):
            print(i,j,k)
            dp[i][j] += dp[k][j-1] * int(comb(i,k))
            # if dp[i][j] > buckets:
              # break
      # dp[1][1] = 44
      print(dp)
      # print(comb(2,3))

solu = Solution()
solu.poorPigs(3, 5, 20)

