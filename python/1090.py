from collections import Counter
from typing import List

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        cnt = Counter()
        ans = 0
        for v, l in sorted(zip(values, labels), reverse=True):
            if cnt[l] < useLimit:
                print(v, l)
                ans += v
                cnt[l] += 1
                numWanted -= 1
                if numWanted == 0:
                    return ans
        return ans


values = [5,4,3,2,1]
labels = [1,1,2,2,3]
numWanted = 3
useLimit = 1
s = Solution()
s.largestValsFromLabels(values, labels, numWanted, useLimit)