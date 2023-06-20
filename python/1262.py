from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = [0, 0, 0]
        for num in nums:
            num1 = ans[0] + num
            num2 = ans[1] + num
            num3 = ans[2] + num
            ans[num1 % 3] = max(ans[num1 % 3], num1)
            ans[num2 % 3] = max(ans[num2 % 3], num2)
            ans[num3 % 3] = max(ans[num3 % 3], num3)
        return ans[0]
