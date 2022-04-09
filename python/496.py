from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]

solu = Solution()
nums1 = [4,1,2,3]
nums2 = [1,3,4,2]
print(solu.nextGreaterElement(nums1, nums2))