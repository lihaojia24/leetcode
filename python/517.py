from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        avg = total // n
        res = 0
        ans = 0
        for machine in machines:
            gap = machine - avg
            res += gap
            ans = max(ans, gap, abs(res))
        return ans


machines = [0,2,0]
solu = Solution()
print(solu.findMinMoves(machines))