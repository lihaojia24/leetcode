from collections import defaultdict
from typing import List


# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         L = 10
#         bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
#         n = len(s)
#         if n <= L:
#             return []
#         res = []
#         key = 0
#         dic = defaultdict(int)
#         for ch in s[:L - 1]:
#             key = (key << 2) | bin[ch]
#         for index in range(L - 1, n):
#             key = ((key << 2) | bin[s[index]]) & ((1 << L * 2) - 1)
#             dic[key] += 1
#             if dic[key] == 2:
#                 res.append(s[index - L + 1 : index + 1])
#         return res

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        MOD = 10**9 + 7
        n = len(s)
        P = 131313
        h = [0] * n
        p = [0] * n
        p[0] = 1
        ans = []
        for i in range(1, n):
            h[i] = h[i - 1] * P + s[i-1]
            p[i] = p[i - 1] * P
        dic = defaultdict(int)
        for i in range(n-10):
            j = i + 9
            hash = h[j] - h[i - 1] * p[j - i + 1]
            cnt = dic[hash]
            if cnt == 1: ans.append(s[i:j+1])
            dic[hash] += 1
        return ans
           


            

solu = Solution()
print(solu.findRepeatedDnaSequences("AAAAAAAAAAAAA"))

