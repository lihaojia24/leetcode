from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        ans = len(arr)
        while left < right and arr[left] <= arr[left+1]:
            left += 1
        left += 1
        if left == len(arr):
            return 0
        while left >= 0:
            while (left == 0 or arr[right] >= arr[left-1]) and (right == len(arr) - 1 or (right > 0 and arr[right] <= arr[right+1])):
                right -= 1
            print(left, right)
            ans = min(ans, right-left+1)
            left -= 1
        return ans
    
arr = [1,2,3,10,4,2,3,5]
s = Solution()
print(s.findLengthOfShortestSubarray(arr))