from typing import List

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        preSum, ans = 0, 0
        nums.sort()
        for num in nums:
            minSum = preSum + num
            ans += (num * num * minSum) % MOD
            preSum += minSum
        return ans % MOD

s = Solution()
nums = [658,489,777,2418,1893,130,2448,178,1128,2149,1059,1495,1166,608,2006,713,1906,2108,680,1348,860,1620,146,2447,1895,1083,1465,2351,1359,1187,906,533,1943,1814,1808,2065,1744,254,1988,1889,1206]
print(s.sumOfPower(nums))