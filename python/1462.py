from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        m = [set() for _ in range(numCourses)]
        for x, y in prerequisites:
            m[x].add(y)
        for i in range(numCourses):
            q = list(m[i])
            while q:
                for _ in range(len(q)):
                    node = q.pop()
                    for y in m[node]:
                        if y not in m[i]:
                            m[i].add(y)
                            q.append(y)
        ans = [y in m[x] for x, y in queries]
        return ans

s = Solution()
numCourses = 4
prerequisites = [[1,2],[1,0],[2,0],[0,3]]
queries = [[1,0],[1,2]]
s.checkIfPrerequisite(numCourses, prerequisites, queries)