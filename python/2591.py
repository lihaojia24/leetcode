class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money > children * 8:
            return children - 1
        if money == children * 8:
            return children
        if money < children:
            return -1
        if money == 4 and children == 1:
            return -1
        money -= children
        ans = money // 7
        if money % 7 == 3 and ans == children - 1:
            ans -= 1
        return ans


