from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def dfs(path, remain):
            # print(path)
            if len(path) == n:
                ans.append(path)
                return
            for i in range(len(remain)):
                dfs(path + [remain[i]], remain[:i] + remain[i+1:])
        dfs([], nums)
        return ans

solu = Solution()
nums = [1,2,3]
print(solu.permute(nums))

            