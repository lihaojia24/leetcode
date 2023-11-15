from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        num = max(nums)
        return (num + num + k - 1) * k / 2