from typing import List

class Solution:
  def isOneBitCharacter(self, bits: List[int]) -> bool:
    i = 0 
    while i < len(bits) - 1:
      i += (1 if bits[i] == 0 else 2)
    return True if i == len(bits) - 1 else False