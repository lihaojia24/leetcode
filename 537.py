#1+1i
class ComplexNumber:
  def __init__(self, num:str) -> None:
    nums = num.split('+')
    self.x = int(nums[0])
    self.y = int(nums[-1][:-1])
  
  def __mul__(self, other):
    x = self.x * other.x - self.y * other.y
    y = self.x * other.y + self.y * other.x
    return ComplexNumber(f'{x}+{y}i')
  
  def __str__(self) -> str:
      return f'{self.x}+{self.y}i'
      
      
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
      cNum1, cNum2 = ComplexNumber(num1), ComplexNumber(num2)
      ans = cNum1 * cNum2
      return str(ans)

num1 = "1+1i"
num2 = "1+1i"
s = Solution()
print(s.complexNumberMultiply(num1, num2))