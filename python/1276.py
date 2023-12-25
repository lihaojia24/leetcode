from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 1:
            return []
        if cheeseSlices * 2 > tomatoSlices or cheeseSlices * 4 < tomatoSlices:
            return []
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        return [x, cheeseSlices - x]