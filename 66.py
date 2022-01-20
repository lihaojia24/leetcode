from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i+1, n):
                    digits[j] = 0
                return digits

        return [1] + [0] * n


solu = Solution()
digits = [1,2,3]
print(solu.plusOne(digits))