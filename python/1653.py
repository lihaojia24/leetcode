class Solution1:
    def minimumDeletions(self, s: str) -> int:
        cnt = s.count('a')
        ans = cnt
        for ch in s:
            cnt += (ord(ch) - ord('a')) * 2 - 1
            ans = min(ans, cnt)
            # if ch == 'a':
            #     cnt -= 1
            #     ans = min(ans, cnt)
            # else:
            #     cnt += 1
        return ans
    
class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        cntB = 0
        for ch in s:
            if ch == 'a':
                ans = min(ans + 1, cntB)
            else:
                cntB+=1
        return ans