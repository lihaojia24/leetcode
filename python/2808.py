from collections import defaultdict
from itertools import pairwise
from typing import List

class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for index, num in enumerate(nums):
            pos[num].append(index)
        ans = n = len(nums)
        for pos_list in pos.values():
            pos_list.append(pos_list[0] + n)
            pos_max_step = max(j - i for i, j in pairwise(pos_list)) // 2
            ans = min(ans, pos_max_step)
        return ans