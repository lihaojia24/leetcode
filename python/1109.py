from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ansRes = [0] * n
        for start, end, seats in bookings:
            ansRes[start - 1] += seats
            if end < n:
                ansRes[end] -= seats
        
        for i in range(1, n):
            ansRes[i] += ansRes[i-1]
        return ansRes