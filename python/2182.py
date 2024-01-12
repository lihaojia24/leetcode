class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        def myord(ch: bytes) -> int:
            return ord(ch) - ord('a')
        def mychr(i: int) -> bytes:
            return chr(ord('a') + i)
        m = [0] * 26
        for ch in s:
            m[myord(ch)] += 1
        io = 25
        ir = 0
        res = ['a'] * len(s)
        while io > -1:
            if m[io] < 1:
                io -= 1
                continue
            if m[io] <= repeatLimit:
                for _ in range(m[io]):
                    res[ir] = mychr(io)
                    ir += 1
                io -= 1
            else:
                for _ in range(repeatLimit):
                    res[ir] = mychr(io)
                    ir += 1
                m[io] -= repeatLimit
                t = io - 1
                while t > -1:
                    if m[t] > 0:
                        break
                    t -= 1
                if t < 0: break
                res[ir] = mychr(t)
                ir += 1
                m[t] -= 1
        return ''.join(res[:ir])
