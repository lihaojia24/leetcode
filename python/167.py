from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            tt = target - numbers[r]
            while numbers[l] < tt:
                l += 1
            if numbers[l] == tt:
                return [l+1, r+1]
            r -= 1
        return [-1, -1]
    
numbers = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(numbers, target))