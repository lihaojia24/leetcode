from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for x, y in zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            v1, v2 = int(x), int(y)
            if v1 != v2:
                return 1 if v1 > v2 else -1
        return 0