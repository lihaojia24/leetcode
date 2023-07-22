from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        account5 = 0
        account10 = 0
        for bill in bills:
            if bill == 5:
                account5 += 1
            elif bill == 10:
                if account5 < 1:
                    return False
                account5 -= 1
                account10 += 1
            elif bill == 20:
                if account5 > 0 and account10 > 0:
                    account5 -= 1
                    account10 -= 1
                elif account5 > 2:
                    account5 -= 3
                else:
                    return False
            print(bill ,account5, account10)
        return True

s = Solution()
bs = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print(s.lemonadeChange(bs))