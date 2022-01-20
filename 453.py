class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min = nums[0]
        sum = 0
        for num in nums:
            sum += num
            min = num if num < min else min
        return sum - min * len(nums)