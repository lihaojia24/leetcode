class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        # s1 = 0
        remain = total
        while remain >= 0:
            ans += (remain // cost2 + 1)
            remain -= cost1
        return ans

s = Solution()
print(s.waysToBuyPensPencils(20,10,5))