import bisect
from collections import defaultdict
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        availables = []
        lakers = {}
        for i, rain in enumerate(rains):
            if rain == 0:
                availables.append(i)
            else:
                ans[i] = -1
                if rain in lakers:
                    print(availables, lakers[rain])
                    ava = bisect.bisect_left(availables, lakers[rain])
                    print(ava)
                    if ava == len(availables):
                        return []
                    else:
                        ans[availables[ava]] = rain
                        availables.remove(availables[ava])
                lakers[rain] = i
        return ans


s = Solution()
print(s.avoidFlood([1,0,2,0,2,1]))