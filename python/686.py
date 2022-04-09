class Solution:
  def KMPNext(self, pattern):
    n = len(pattern)
    res = [0] * n
    for index in range(1, n):
      tmp = index - 1
      while pattern[tmp] != pattern[index] and tmp != 0:
        tmp = res[tmp-1]
      if pattern[tmp] == pattern[index]:
        res[index] = tmp + 1
      else:
        res[index] = 0
    return res





  # def repeatedStringMatch(self, a: str, b: str) -> int:

solu = Solution()
print(solu.KMPNext('aaabbab'))


class Solution:
    def strstr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        k1 = 10 ** 9 + 7
        k2 = 1337
        mod1 = randrange(k1) + k1
        mod2 = randrange(k2) + k2

        hash_needle = 0
        for c in needle:
            hash_needle = (hash_needle * mod2 + ord(c)) % mod1
        hash_haystack = 0
        for i in range(m - 1):
            hash_haystack = (hash_haystack * mod2 + ord(haystack[i % n])) % mod1
        extra = pow(mod2, m - 1, mod1)
        for i in range(m - 1, n + m - 1):
            hash_haystack = (hash_haystack * mod2 + ord(haystack[i % n])) % mod1
            if hash_haystack == hash_needle:
                return i - m + 1
            hash_haystack = (hash_haystack - extra * ord(haystack[(i - m + 1) % n])) % mod1
            hash_haystack = (hash_haystack + mod1) % mod1
        return -1

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        index = self.strstr(a, b)
        if index == -1:
            return -1
        if n - index >= m:
            return 1
        return (m + index - n - 1) // n + 2

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/repeated-string-match/solution/zhong-fu-die-jia-zi-fu-chuan-pi-pei-by-l-vnye/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。