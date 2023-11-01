class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        res = [0] * 10
        for i in range(0, n, 2):
            pos = ord(rings[i+1]) - ord('0')
            if rings[i] == 'R':
                res[pos] |= 1 
            if rings[i] == 'G':
                res[pos] |= 1 << 1
            if rings[i] == 'B':
                res[pos] |= 1 << 2
        return sum( 1 if num == 7 else 0 for num in res)