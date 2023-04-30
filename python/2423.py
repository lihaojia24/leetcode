class Solution:
    def equalFrequency(self, word: str) -> bool:
        m = {}
        for ch in word:
            v = m.get(ch, 0)
            m[ch] = v + 1
        if len(m) == 1:
            return True
        vs = list(m.values())
        vs.sort()
        if vs[0] == 1 and vs[1] == vs[-1]:
            return True
        if vs[0] == vs[-2] and vs[0] + 1 == vs[-1]:
            return True
        return False
        
