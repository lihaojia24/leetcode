from typing import List
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(ring)
        MAX_INT = 1e9
        ch2pos = {}
        for pos, ch in enumerate(ring):
            if ch in ch2pos:
                ch2pos[ch].append(pos)
            else:
                ch2pos[ch] = [pos]
        def findNext(pre_pos: List[List[int]], target: str) -> List[List[int]]:
            res = []
            for pos in ch2pos[target]:
                n_pos = [pos, MAX_INT]
                for p_pos in pre_pos:
                    dis = min((p_pos[0] - pos) % N, (pos - p_pos[0]) % N)
                    n_pos[1] = min(n_pos[1], p_pos[1] + dis + 1)
                res.append(n_pos)
            return res
        pos = [[0, 0]]
        for target in key:
            pos = findNext(pos, target)
        res = pos[0][1]
        for p in pos:
            res = min(res, p[1])
        return res