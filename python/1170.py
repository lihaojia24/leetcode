from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word: str) -> int:
            cnt, flag = 1, word[0]
            for ch in word[1:]:
                if ord(ch) < ord(flag):
                    cnt, flag = 1, ch
                elif ch == flag:
                    cnt += 1
            return cnt
        ans = []
        queries = [f(q) for q in queries]
        words = [f(w) for w in words]
        print(queries, words)
        words.sort(reverse=True)
        for q in queries:
            for i in range(len(words)):
                if q >= words[i]:
                    ans.append(i)
                    break
                elif i == len(words) - 1:
                    ans.append(len(words))
        return ans

qs = ["cbd"]
ws = ["zaaaz"]
s = Solution()
print(s.numSmallerByFrequency(qs, ws))
    