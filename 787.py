from typing import List

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         # dp[t][i] t: times i: terminal index
#         dp = [[float("inf")] * n for _ in range(k+2)]
#         dp[0][src] = 0
#         for t in range(1, k+2):
#             for x, y, cost in flights:
#                 dp[t][y] = min(dp[t][y], dp[t-1][x] + cost)
#         res = [dp[i][dst] for i in range(1, k+2)]
#         ans = min(res)
#         return -1 if ans == float("inf") else ans

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dp[t][i] t: times i: terminal index
        dp = [float("inf")] * n
        dp[src] = 0
        res = float("inf")
        for t in range(1, k+2):
            dpNex = [float("inf")] * n
            for x, y, cost in flights:
                dpNex[y] = min(dpNex[y], dp[x] + cost)
            dp = dpNex
            res = min(res, dp[dst])
        return -1 if res == float("inf") else res

flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
solu = Solution()
print(solu.findCheapestPrice(5, flights, 2, 1, 1))