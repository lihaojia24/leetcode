class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()
        x = 1 % k
        while x and x not in seen:
            seen.add(x)
            x = (x * 10 + 1) % k
        return -1 if x else len(seen) + 1

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/smallest-integer-divisible-by-k/solution/san-chong-suan-fa-you-hua-pythonjavacgo-tk4cj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。