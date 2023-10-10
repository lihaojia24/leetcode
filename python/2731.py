from typing import List

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10 ** 9 + 7
        for i, ch in enumerate(s):
            nums[i] += d if ch == 'R' else -d
        nums.sort()
        tmp = 0
        ans = 0
        for i, num in enumerate(nums):
            ans += i * num - tmp
            tmp += num
        return ans % MOD