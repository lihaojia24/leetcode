singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]


class Solution:
    def numberToWords(self, num: int) -> str:
        def toEngilsh(num: int) -> str:
            s = ""
            if num >= 100:
                s += singles[num // 100] + " Handred "
                num %= 100
            if num >= 20:
                s += tens[num // 10] + " "
                num %= 10
            if num >= 10:
                s += teens[num // 10] + " "
            elif 0 < num < 10:
                s += singles[num] + " "
            return s

        if num == 0:
            return "Zero"
        
        s = ""
        unit = int(1e9)
        for i in range(3, -1, -1):
            curNum = num // unit
            if curNum:
                num %= unit
                s += toEngilsh(curNum) + thousands[i] + " "
            unit //= 1000
        return s.strip()
