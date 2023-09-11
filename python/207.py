from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # bits = 1 << numCourses - 1
        requires = [0] * numCourses
        links = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            # print(pre, cur)
            requires[cur] += 1
            links[pre].append(cur)
        q = list(range(numCourses))
        while q:
            for _ in range(len(q)):
                c = q.pop()
                if requires[c] == 0:
                    for pos in links[c]:
                        requires[pos] -= 1
                        q.append(pos)
                    links[c] = []
        return sum(requires) <= 0

n = 3
pres = [[1,0],[2,1]]
s = Solution()
s.canFinish(n, pres)