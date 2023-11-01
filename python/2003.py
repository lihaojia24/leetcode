from typing import List

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        if min(nums) > 1: return ans
        startNode = nums.index(1)
        m = [[] for _ in range(n)]
        for i in range(1, n):
            m[parents[i]].append(i)
        vis = set()
        def dfs(i: int) -> None:
            vis.add(nums[i])
            for c in m[i]:
                if nums[c] not in vis:
                    dfs(c)
        mex = 2
        while startNode >= 0:
            dfs(startNode)
            while mex in vis:
                mex += 1
            ans[startNode] = mex
            startNode = parents[startNode]
        return ans