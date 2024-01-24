from typing import List
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        # from left 
        s = 0
        max_from_left = [0] * n
        sum_from_left = [0] * n
        for i, maxHeight in enumerate(maxHeights):
            pre_index = i - 1
            while pre_index > -1 and max_from_left[pre_index] > maxHeight:
                s -= max_from_left[pre_index]
                s += maxHeight
                max_from_left[pre_index] = maxHeight
                pre_index -= 1
            s += maxHeight
            max_from_left[i] = maxHeight
            sum_from_left[i] = s

        # from right
        s = 0
        max_from_right = [0] * n
        sum_from_right = [0] * n
        for i in range(n-1, -1, -1):
            maxHeight = maxHeights[i]
            pre_index = i + 1
            while pre_index < n and max_from_right[pre_index] > maxHeight:
                s -= max_from_right[pre_index]
                s += maxHeight
                max_from_right[pre_index] = maxHeight
                pre_index += 1
                
            s += maxHeight
            max_from_right[i] = maxHeight
            sum_from_right[i] = s
        # res
        res = 0
        for rmax, lmax, hmax in zip(sum_from_right, sum_from_left, maxHeights):
            res = max(res, rmax + lmax - hmax)
        return res