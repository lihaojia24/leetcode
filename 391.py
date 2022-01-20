from typing import DefaultDict, List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, minx, miny, maxx, maxy = 0, rectangles[0][0], rectangles[0][1], rectangles[0][2], rectangles[0][3]
        cnt = DefaultDict(int)
        for rec in rectangles:
            x, y, a, b = rec[0], rec[1], rec[2], rec[3]
            area += (b - y) * (a - x)

            minx, miny, maxx, maxy = min(minx, x), min(miny, y), max(maxx, a), max(maxy, b)

            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        if area != (maxy - miny) * (maxx - minx) or cnt[(minx, miny)] != 1 or cnt[(minx, maxy)] != 1 or cnt[(maxx, miny)] != 1 or cnt[(maxx, maxy)] != 1:
            return False
        
        del cnt[(minx, miny)], cnt[(minx, maxy)], cnt[(maxx, miny)], cnt[(maxx, maxy)]

        return all(c == 2 or c == 4 for c in cnt.values())