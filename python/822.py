from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        fb = { x for x, y in zip(fronts, backs) if x == y}
        return min((x for x in fronts + backs if x not in fb),default=0)