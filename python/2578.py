class Solution:
    def splitNum(self, num: int) -> int:
        li = []
        while num > 0:
            li.append(num % 10)
            num //= 10
        li.sort()
        ans = [0, 0]
        for i,nu in enumerate(li):
            ans[i%2] = ans[i%2] * 10 + nu
        return ans[0] + ans[1]
