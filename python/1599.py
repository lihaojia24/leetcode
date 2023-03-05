from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        wait = 0
        earn = 0
        maxEarn = earn
        ans = -1
        i = 0
        while i < len(customers) or wait > 0:
            if i < len(customers):
                wait += customers[i]
            passanger = min(wait, 4)
            wait -= passanger
            earn += passanger * boardingCost - runningCost
            if earn > maxEarn:
                earn = maxEarn
                ans = i
            i+=1
        return ans+1 if ans != -1 else -1

    
s = Solution()
customers = [8,3,8]
boardingCost = 5
runningCost = 6
print(s.minOperationsMaxProfit(customers, boardingCost, runningCost))