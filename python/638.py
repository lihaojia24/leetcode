from typing import List
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], specials: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        specials_filited = []
        for special in specials:
            if sum(special[:-1]) > 0 and sum([special[i] * price[i] for i in range(n)]) > special[-1]:
                specials_filited.append(special)
        
        @lru_cache(None)
        def dfs(cur_needs):
            min_price = sum([cur_needs[i] * price[i] for i in range(n)])
            for special in specials_filited:
                special_price = special[-1]
                nxt_needs = []
                for i in range(n):
                    if special[i] > cur_needs[i]:
                        break
                    nxt_needs.append(cur_needs[i] - special[i])
                if len(nxt_needs) == n:
                    min_price = min(min_price, dfs(tuple(nxt_needs)) + special_price)
            return min_price
        
        return dfs(tuple(needs))

solu = Solution()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]

print(solu.shoppingOffers(price, special, needs))
