# import heapq

# class MedianFinder:

#     def __init__(self):
#         self.minList = list()
#         self.maxList = list()


#     def addNum(self, num: int) -> None:
#         if not self.maxList or num >= self.maxList[0]:
#             heapq.heappush(self.maxList, num)
#             if len(self.maxList) > len(self.minList) + 1:
#                 heapq.heappush(self.minList, -1 * heapq.heappop(self.maxList))
#         else:
#             heapq.heappush(self.minList, -1 * num)
#             if len(self.minList) > len(self.maxList):
#                 heapq.heappush(self.maxList, -1 * heapq.heappop(self.minList))



#     def findMedian(self) -> float:
#         if len(self.maxList) > len(self.minList):
#             return self.maxList[0]
#         return (-self.minList[0] + self.maxList[0]) / 2


from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = SortedList()


    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        return self.nums[n // 2] if n % 2 else (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2
        # return (self.nums[n // 2] + self.nums[n // 2 - 1]) / 2 if n % 2 else self.nums[n // 2]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
# obj.addNum(2)
# obj.addNum(3)
obj.addNum(4)
param_2 = obj.findMedian()
print(param_2)