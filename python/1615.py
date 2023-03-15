from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ins = [0] * n
        link = [[0] * n for _ in range(n)]
        for road in roads:
            ins[road[0]] += 1
            ins[road[1]] += 1
            link[road[0]][road[1]] = 1
            link[road[1]][road[0]] = 1
        ans = 0
        tmp = 0
        for i in range(n):
            for j in range(n):
                tmp = ins[i] + ins[j] - link[i][j]
                ans = tmp if tmp > ans else ans
        return ans
