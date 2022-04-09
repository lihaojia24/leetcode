from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        def dfs(path, remain):
            if len(path) == n:
                ans.append(path)
                return
            for i in range(len(remain)):
                if i > 0 and remain[i] == remain[i-1]:
                    continue
                dfs(path + [remain[i]], remain[:i] + remain[i+1:])
        dfs([], nums)
        return ans

solu = Solution()
nums = [1,1,2]
print(solu.permuteUnique(nums))