class Solution:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        for i in range(n-1):
            tmp = ""
            count = 0
            tag = ""
            for ch in prev:
                if ch == tag:
                    count += 1
                else:
                    if tag:
                        tmp += str(count)
                        tmp += tag
                    tag = ch
                    count = 1
            if tag:
                tmp += str(count)
                tmp += tag
            prev = tmp
            print(prev)
        return prev

solu = Solution()
print(solu.countAndSay(5))