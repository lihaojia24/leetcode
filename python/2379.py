class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        tmp = 0
        for i in range(k):
            if blocks[i] == 'W': tmp+=1
        ans = tmp
        l, r = 0, k
        while r < len(blocks):
            if blocks[l] == 'W': tmp-=1
            if blocks[r] == 'W': tmp+=1
            ans = min(ans, tmp)
            l+=1
            r+=1
        return ans
