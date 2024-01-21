from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        r = sum(nums)
        l = max(nums)
        while l < r:
            # 计算x
            m = (l + r) // 2
            cnt = 1
            s = 0
            for num in nums:
                if s + num > m:
                    cnt += 1
                    s = num
                else:
                    s += num
            if cnt > k:
                l = m + 1
            else:
                r = m
        return l
