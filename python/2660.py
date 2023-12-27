from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1, s2 = 0, 0
        bouns1, bouns2 = 0, 0
        for p1, p2 in zip(player1, player2):
            s1 += 2 * p1 if bouns1 > 0 else p1
            s2 += 2 * p2 if bouns2 > 0 else p2
            bouns1 = 2 if p1 == 10 else bouns1 - 1
            bouns2 = 2 if p2 == 10 else bouns2 - 1
        if s1 > s2: return 1
        if s1 < s2: return 2
        return 0
