import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/ransom-note/solution/shu-jin-xin-by-leetcode-solution-ji8a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。