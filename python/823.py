from functools import cache
from typing import List

class Solution:

# 116 ms
# 16.2 MB
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        idx = {x : i for i, x in enumerate(arr)}
        ans = [1] * len(arr)
        for i, val in enumerate(arr):
            for j in range(i):
                x = arr[j]
                if x * x < val:
                    if val % x == 0 and val // x in idx:
                        ans[i] += ans[j] * ans[idx[val // x]] * 2
                if x * x == val:
                    ans[i] += ans[j] * ans[j]
                    break
                else:
                    break
        return sum(ans) % (10 ** 9 + 7)

class Solution2:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        idx = {x : i for i, x in enumerate(arr)}
        ans = [1] * len(arr)
        for i, val in enumerate(arr):
            for j in range(i):
                x = arr[j]
                if val % x == 0 and val // x in idx:
                    ans[i] += ans[j] * ans[idx[val // x]]
        return sum(ans) % (10 ** 9 + 7)


class Solution1:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arrS = set(arr)
        @cache
        def dfs(val: int) -> int:
            res = 1
            for x in arr:
                if val % x == 0 and val // x in arrS:
                    res += dfs(x) * dfs(val // x)
            return res
        return sum(dfs(x) for x in arr) % (10 ** 9 + 7)