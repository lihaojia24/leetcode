class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(n, 0, -1):
            if not bin(i)[2:] in s:
                return False
        return True
        # return all([bin(i)[2:] in s for i in range(n, 0, -1)])