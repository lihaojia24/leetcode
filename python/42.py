from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftList, rightList = [0] * n, [0] * n
        leftList[0], rightList[-1] = height[0], height[-1]
        for i in range(1, n):
            leftList[i] = max(height[i], leftList[i - 1])
            rightList[n-1 - i] = max(height[n-1 - i], rightList[n - i])
        for i in range(0, n):
            leftList[i] = min(leftList[i], rightList[i])
        print(leftList)
        ans = sum([leftList[i] - height[i] for i in range(0, n)])
        return ans