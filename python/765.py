from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        pos = [0] * n
        for index, p in enumerate(row):
            pos[p] = index
        ans = 0
        for i in range(0, n , 2):
            if row[i] ^ row[i + 1] != 1:
                ans += 1
                row[pos[row[i] ^ 1]] = row[i+1]
                pos[row[i+1]] = pos[row[i] ^ 1]
        return ans