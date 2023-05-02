from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i, j = 0, 0
        ans = set()
        py = [1]
        while y != 1 and pow(y, j) <= bound - 1:
                j += 1   
                py.append(pow(y, j))
                print(j)
        while(pow(x, i) < bound):
            xi = pow(x, i)
            while pow(y, j) > bound - xi:
                j -= 1
            print(py)
            ans.update([xi + b for b in py[:j+1]])
            i += 1
            if x == 1: break
        return list(ans)
    
x = 1
y = 2
bound = 10
s = Solution()
print(s.powerfulIntegers(x,y,bound))
