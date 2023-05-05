from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        maxTime, ans = 0, 0
        time = 0
        for (id, endTime) in logs:
            t = endTime - time
            if t > maxTime:
                maxTime = t
                ans = id
            elif t == maxTime:
                ans = min(ans, id)
            time = endTime
        return ans
    
logs = [[1,1],[3,7],[2,12],[7,17]]
n = 10
s = Solution()
print(s.hardestWorker(n, logs))