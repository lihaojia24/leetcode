from typing import DefaultDict, List

class Solution:
    def longestSubsequence(self, nums: List[int], difference: int) -> int:
        ans = DefaultDict(int)
        for num in nums:
            ans[num] = ans[num - difference] + 1
        print(ans)
        return max(ans.values())

solu = Solution()
nums = [1,3,5,7]
print(solu.longestSubsequence(nums, 1))