from typing import Tuple

# class Solution:
#     def reorderedPowerOf2(self, n: int) -> bool:
#         def isValid(num):
#             return num > 0 and (num & (num - 1) == 0)
#         nums = sorted(list(str(n)))
#         n = len(nums)
#         def dfs(path, remain):
#             if len(path) == n:
#                 if isValid(int(''.join(path))):
#                     return True
#             if len(path) > 0 and path[0] == '0':
#                 pass
#             else:
#                 for i in range(len(remain)):
#                     if dfs(path + [remain[i]], remain[:i] + remain[i+1:]):
#                         return True
#             return False
#         return dfs([], nums)




        
def countDigits(n: int) -> Tuple[int]:
    cnt = [0] * 10
    while n:
        cnt[n % 10] += 1
        n //= 10
    return tuple(cnt)

allList = {countDigits(1 << i) for i in range(30)}

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return countDigits(n) in allList


solu = Solution()
nums = 1
print(solu.reorderedPowerOf2(nums))

