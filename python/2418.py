from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        s = list(range(len(names)))
        s.sort(key=lambda x: heights[x], reverse=True)
        ans = []
        for i in s:
            ans.append(names[i])
        return ans