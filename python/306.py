class Solution:
  def isAdditiveNumber(self, num: str) -> bool:
    n = len(num)
    fStart = 0
    for sStart in range(1, n):
      fEnd = sStart - 1
      if num[fStart] == '0' and fEnd != 0:
        break # return False
      for sEnd in range(sStart, n):
        if num[sStart] == '0' and sEnd != sStart:
          break
        if self.isValid(num, sStart, sEnd):
          return True
    return False

  def isValid(self, num, sStart, sEnd):
    n = len(num)
    fStart, fEnd = 0, sStart - 1
    while sEnd <= n - 1:
      third = self.strAdd(num, fStart, fEnd, sStart, sEnd)
      tStart = sEnd + 1
      tEnd = tStart + len(third) - 1
      if tEnd > n - 1 or num[tStart: tEnd + 1] != third:
        break # return False
      elif tEnd == n - 1:
        return True
      fStart, fEnd = sStart, sEnd
      sStart, sEnd = tStart, tEnd
    return False

  def strAdd(self, num, fStart, fEnd, sStart, sEnd):
    carry, cur = 0, 0
    third = []
    while fStart <= fEnd or sStart <= sEnd or carry != 0:
      cur = carry
      if fStart <= fEnd:
        cur += ord(num[fEnd]) - ord('0')
        fEnd -= 1
      if sStart <= sEnd:
        cur += ord(num[sEnd]) - ord('0')
        sEnd -= 1
      carry = cur // 10
      cur = cur % 10
      third.append(chr(cur + ord('0')))
    return ''.join(third[::-1])

    
