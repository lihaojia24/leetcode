from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        step = n // 2
        index = step
        while (index > 0 and arr[index] < arr[index - 1]) or (index < n - 1 and arr[index] < arr[index + 1]):
            print(index)
            step = max(1, step // 2)
            if index > 0 and arr[index] < arr[index - 1]:
                index -= step
            else:
                index += step
        return index
    
solu = Solution()

arr = [24,69,100,99,79,78,67,36,26,19]
print(solu.peakIndexInMountainArray(arr))