from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        actions = []
        for num, fr, to in trips:
            actions.append((fr, num))
            actions.append((to, -num))
        actions.sort(key=lambda x: (x[0], x[1]))
        passenger = 0
        for action in actions:
            passenger += action[1]
            if passenger > capacity:
                return False
        return True
