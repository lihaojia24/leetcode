from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l, r = 0, 0
        while seats[l] == 0: l += 1
        while seats[-r - 1] == 0: r += 1
        tmp, mx, n = 0, 0, len(seats)
        for i in range(l, n - r):
            print(seats[i])
            if seats[i]:
                mx = max(mx, tmp)
                tmp = 0
            else:
                tmp += 1
        print(l, r, mx)
        return max(l, r, (mx + 1) // 2)

s = Solution()
print(s.maxDistToClosest([1,0,0,0]))