from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        index = 0
        while candies > 0:
            ans[index%num_people] += min(candies, index + 1)
            candies -= index + 1
            index += 1
        return ans