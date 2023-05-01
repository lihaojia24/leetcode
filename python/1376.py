from collections import deque
from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        m = {}
        q = deque([[headID, 0]])
        ans = 0
        for i, f in enumerate(manager):
            m[f] = m.get(f, [])
            m[f].append(i)
        while(q):
            id, time = q.popleft()
            if m.get(id):
                for cid in m[id]:
                    ctime = time + informTime[id]
                    ans = max(ans, ctime)
                    q.append([cid, ctime])
        return ans

n = 6
headId = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
s = Solution()
print(s.numOfMinutes(n, headId, manager, informTime))