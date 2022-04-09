
from heapq import heappop, heappush
from os import times
from sqlite3 import Timestamp


class StockPrice:

  def __init__(self):
    self.maxPrice = []
    self.minPrice = []
    self.time2price = {}
    self.maxTime = 0

  def update(self, timestamp: int, price: int) -> None:
    self.time2price[timestamp] = price
    self.maxTime = max(self.maxTime, timestamp)
    heappush(self.maxPrice, [-price, timestamp])
    heappush(self.minPrice, [price, timestamp])

  def current(self) -> int:
    return self.time2price[self.maxTime]

  def maximum(self) -> int:
    while True:
      price, timestamp = self.maxPrice[0]
      if -price == self.time2price[timestamp]:
        return -price
      heappop(self.maxPrice)

  def minimum(self) -> int:
    while True:
      price, timestamp = self.minPrice[0]
      if price == self.time2price[timestamp]:
        return price
      heappop(self.minPrice)



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

from sortedcontainers import SortedList
class StockPrice:

  def __init__(self):
    self.price = SortedList()
    self.time2price = {}
    self.maxTime = 0

  def update(self, timestamp: int, price: int) -> None:
    if timestamp in self.time2price:
      self.price.discard(self.time2price[timestamp])
    self.price.add(price)
    self.time2price[timestamp] = price
    self.maxTime = max(self.maxTime, timestamp)


  def current(self) -> int:
    return self.time2price[self.maxTime]

  def maximum(self) -> int:
    return self.price[-1]

  def minimum(self) -> int:
    return self.price[0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()