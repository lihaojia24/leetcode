from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0: return ans
        start = nums[0]
        end = nums[0]
        for num in nums[1:]:
            if num != end+1:
                if end == start:
                    ans.append(end)
                else:
                    ans.append(str(start) + "->" + str(end))
                start = num
            end = num
        if end == start:
            ans.append(end)
        else:
            ans.append(str(start) + "->" + str(end))
        return ans