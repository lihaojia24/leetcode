from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        
        for num in nums:
            # 存在则+1
            if num in dic.keys():
                dic[num] += 1
            # 不存在，字典没填满，添加进字典
            elif len(dic) < 2:
                dic[num] = 1
            # 不存在，字典已满，所有key的value-1,key为0则删除
            else:
                for key in list(dic.keys()):
                    dic[key] -= 1
                    if dic[key] == 0:
                        dic.pop(key)
            # print(dic)
        for key in dic.keys():
            dic[key] = 0
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
        res = []
        for key in dic.keys():
            if dic[key] > len(nums) / 3:
                # print(key, dic[key])
                res.append(key)

        return res

solu = Solution()
nums = [1,1,1,3,3,2,2,2]
print(solu.majorityElement(nums))