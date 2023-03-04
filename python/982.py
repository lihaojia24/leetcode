from collections import Counter
from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        m = Counter(a & b for a in nums for b in nums)
        return sum(n for x, n in m.items() for c in nums if x & c == 0)


s = Solution()
print(s.countTriplets([2,1,3]))