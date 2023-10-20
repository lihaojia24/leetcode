class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        x = length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 10**9
        y = mass >= 100
        if x and y: return "Both"
        if x: return "Bulky"
        if y: return "Heavy"
        return "Neither"