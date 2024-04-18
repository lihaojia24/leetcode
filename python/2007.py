from collections import Counter
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        cnt0 = cnt.pop(0, 0)
        if cnt0 % 2:
            return []
        ans = [0] * (cnt0 // 2)
        done = set()
        for x in cnt:
            if x in done or x % 2 == 0 and x // 2 in cnt:
                continue
            while x in cnt:
                cnt_x = cnt[x]
                if cnt_x > cnt[2 * x]:
                    return []
                ans.extend([x] * cnt_x)
                done.add(x)
                cnt[2 * x] -= cnt_x
                if cnt[2 * x] == 0:
                    done.add(2*x)
                    x*=4
                else:
                    x *= 2
        return ans