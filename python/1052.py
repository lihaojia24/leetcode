from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = 0
        no_grumpy_adder = 0
        no_grumpy_adder_max = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
            else:
                no_grumpy_adder += customers[i]
            if i >= minutes:
                if customers[i-minutes] == 1:
                    no_grumpy_adder -= customers[i-minutes]
            no_grumpy_adder_max = max(no_grumpy_adder, no_grumpy_adder_max)
        return res + no_grumpy_adder_max