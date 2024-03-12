class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        cnt = s.count('1') - 1
        return '1' * cnt + '0' * (n - cnt - 1) + '1'