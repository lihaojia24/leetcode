from typing import List, Text
import heapq, random

# class Solution:
#     def smallestK(self, arr: List[int], k: int) -> List[int]: 
#         if 0 == k:
#             return []
#         hp = [-1 * i for i in arr[:k]]
#         heapq.heapify(hp)
#         for i in range(k, len(arr)):
#             if -1 * hp[0] > arr[i]:
#                 heapq.heappop(hp)
#                 heapq.heappush(hp, -1 * arr[i])
#         res = [-1 * i for i in hp]
#         return res

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]: 
        if 0 == k:
            return []
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]

    def partition(self, arr, left, right):
        target = arr[right]
        tmp_index = left - 1
        for i in range(left, right):
            if arr[i] <= target:
                tmp_index += 1
                arr[tmp_index], arr[i] = arr[i], arr[tmp_index]
        arr[tmp_index + 1], arr[right] = arr[right], arr[tmp_index + 1]
        return tmp_index + 1

    def random_partition(self, arr, left, right):
        i = random.randint(left, right)
        arr[i], arr[right] = arr[right], arr[i]
        return self.partition(arr, left, right)

    def randomized_selected(self, arr, left, right, k):
        i = self.random_partition(arr, left, right)
        if i < k:
            self.randomized_selected(arr, i+1, right, k)
        elif i > k:
            self.randomized_selected(arr, left, i-1, k)
