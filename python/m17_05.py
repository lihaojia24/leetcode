from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        endIndex = -1
        maxLength = 0
        m = {0:-1}
        sum = 0
        for i, s in enumerate(array):
            if '0' <= s[0] <= '9':
                sum += 1
            else:
                sum -= 1
            print(m)
            print(sum)
            if sum in m:
                if i - m[sum] > maxLength:
                    maxLength = i - m[sum]
                    endIndex = i
            else:
                m[sum] = i
        print(endIndex, maxLength)
        if maxLength == 0:
            return []
        return array[endIndex-maxLength+1:endIndex+1]
    
s = Solution()
print(s.findLongestSubarray(["A","1"]))