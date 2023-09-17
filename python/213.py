from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(nums: List[int]) -> int:
            n = len(nums)
            covers = [0] * n
            nCovers = [0] * n
            covers[0] = nums[0]
            for i, num in enumerate(nums[1:]):
                covers[i+1] = nCovers[i] + num
                nCovers[i+1] = max(covers[i], nCovers[i])
            # print(covers, nCovers) 
            return max(covers[-1], nCovers[-1])
        return max(help(nums[1:]), help(nums[:-1])) if len(nums) > 1 else nums[0]
     
nums = [1,3,1,3,100]
s = Solution()
print(s.rob(nums))