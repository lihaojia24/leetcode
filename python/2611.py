from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        ans = sum(reward2)
        reward1 = [(r1 - r2, i) for i ,(r1, r2) in enumerate(zip(reward1, reward2))]
        reward1.sort(key = lambda x: x[0], reverse=True)
        for i in range(k):
            ans += reward1[i][0]
        return ans
        

s = Solution()
reward1 = [1,1,3,4]
reward2 = [4,4,1,1]
k = 2

print(s.miceAndCheese(reward1, reward2, k))