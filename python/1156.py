from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        text = text + '##'
        if len(text) == 0: return 0
        if len(text) == 1: return 1
        start = 0
        tmp = 0
        end = 1
        flag = True
        ans = 1
        ansCh = text[start]
        cnt = Counter(text)
        while end < len(text):
            print(text[start], text[end])
            if text[end] != text[start]:
                if flag: 
                    flag = False
                    tmp = end
                else: 
                    ch = text[start]
                    mx = min(end-start, cnt[ch])
                    if mx > ans:
                        ans = mx
                        ansCh = ch
                    flag = True
                    start = tmp
                    end = tmp
            end += 1
        print(ansCh)
        return min(ans, cnt[ansCh])
    
s = Solution()
tx = "abbccbcaaa"
print(s.maxRepOpt1(tx))