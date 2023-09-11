from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        pos = -1
        for i, f in enumerate(forts):
            if 0 != f:
                if -1 != pos and f != forts[pos]:
                    ans = max(ans, i - pos - 1)
                pos = i
        return ans