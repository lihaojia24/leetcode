from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        for res in restaurants:
            can = True if veganFriendly == 0 else res[2] == 1
            can = can and maxPrice >= res[3]
            can = can and maxDistance >= res[4]
            if can: ans.append((res[1], res[0]))
        ans.sort(key = lambda x: (x[0], x[1]), reverse=True)
        ans = map(lambda x: x[1], ans)
        return list(ans)

s = Solution()
s.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10)
