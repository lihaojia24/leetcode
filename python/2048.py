from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(n: int) -> bool:
            count = Counter(str(n))
            if all(count[d] == int(d) for d in count):
                return True
        n += 1
        while n < 1224445:
            if check(n):
                return n
            n += 1