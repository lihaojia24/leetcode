from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        remain = k % total
        for index in range(len(chalk)):
            remain -= chalk[index]
            if remain < 0:
                return index
        return -1


chalk = [3,4,1,2]
k = 25
solu = Solution()
print(solu.chalkReplacer(chalk, k))