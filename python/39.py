from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        path = []
        candidates.sort()
        def dfs(i, left: int) -> None:
            if i >= n or candidates[i] > left:
                return 
            if candidates[i] == 0:
                ans.append(path)
                return
            dfs(i + 1, left)
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            
        dfs(0, target)
        return ans