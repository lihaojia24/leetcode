from typing import List

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = [x * i for i in range(n)]
        costs = [num for num in nums]
        for i in range(n):
            for j in range(n):
                costs[j] = min(costs[j], nums[j+i])
            ans[i] += sum(costs)
        return min(ans)