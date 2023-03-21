
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.check(a,b) or self.check(b,a)

    def check(self, a, b) -> bool:
        right = len(a) // 2
        left = right + len(a) % 2 - 1
        while a[left] == a[right]:
            if left == 0:
                return True
            left -= 1
            right += 1
        if a[left] == b[right]:
            t_left = left
            t_right = right
            while a[t_left] == b[t_right]:
                if t_left == 0:
                    return True
                t_left -= 1
                t_right += 1
        if b[left] == a[right]:
            t_left = left
            t_right = right
            while b[t_left] == a[t_right]:
                if t_left == 0:
                    return True
                t_left -= 1
                t_right += 1
        return False

s = Solution()
a = 'aaber'
b = 'fecab'
print(s.checkPalindromeFormation(a,b))