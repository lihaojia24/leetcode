from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        ans = [0] * 26
        for index, ch in enumerate(s):
            i = ord(ch)-ord('a')
            if ans[i] == 0:
                ans[i] = index + 1
            else:
                if distance[i] != index - ans[i]:
                    return False
        return True