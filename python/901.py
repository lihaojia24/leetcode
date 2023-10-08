from math import inf


class StockSpanner:

    def __init__(self):
        self.stack = [(-1, inf)]
        self.cur_day = -1

    def next(self, price: int) -> int:
        while self.stack[-1][1] <= price:
            self.stack.pop()
        self.cur_day += 1
        self.stack.append((self.cur_day, price))
        return self.cur_day - self.stack[-2][0]



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)