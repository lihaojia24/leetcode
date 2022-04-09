class Solution:
    def findComplement(self, num: int) -> int:
        highbit = 0
        while num >= (1 << highbit):
            highbit += 1

        print(highbit)
        mask = (1 << highbit) - 1
        print(mask)

        return mask ^ num

solu = Solution()
print(solu.findComplement(1))