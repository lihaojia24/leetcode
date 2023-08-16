from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        tAns = [1] * n
        i,step = 0, 1
        while tAns[i] == 1:
            tAns[i] = 0
            i = (i + step * k) % n
            step += 1
        return [i+1 for i in range(n) if tAns[i]]