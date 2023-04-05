from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        while i > 0:
            if arr[i-1] > arr[i]:
                tmp = j = i
                while tmp < len(arr):
                    if arr[tmp] > arr[j] and arr[tmp] < arr[i-1]:
                        j = tmp
                    tmp+=1
                # print(i-1, j)
                arr[i-1], arr[j] = arr[j], arr[i-1]
                break
            i-=1
        return arr
    
s = Solution()
arr = [1,9,4,6,7]
print(s.prevPermOpt1(arr))