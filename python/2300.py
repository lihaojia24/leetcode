from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()
        def find(spell: int) -> int:
            if spell * potions[-1] < success: return n
            l, r = 0, n - 1
            while l < r:
                mid = (l + r) >> 1
                if spell * potions[mid] < success:
                    l = mid + 1
                else:
                    r = mid
            return l
        ans = []
        for spell in spells:
            index = find(spell)
            ans.append(n - index)
        return ans