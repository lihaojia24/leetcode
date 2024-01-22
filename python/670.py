class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                mxj = i + 1
                j = i + 1
                while j < len(nums):
                    if nums[j] >= nums[mxj]:
                        mxj = j
                    j += 1
                l, r = 0, i
                while l < r :
                    m = (l + r) // 2
                    if nums[m] >= nums[mxj]:
                        l = m + 1
                    else:
                        r = m
                nums[l], nums[mxj] = nums[mxj], nums[l]
                break
            i += 1
        return int(''.join(nums))
            
            