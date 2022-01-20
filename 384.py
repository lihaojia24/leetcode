from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = self.nums.copy()
        for i in range(self.n):
            j = random.randrange(i, self.n)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
        


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_1, param_2)