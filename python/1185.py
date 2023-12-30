# class Solution:
#   def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
#     res = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
#     days = 0 
#     days += 365 * (year - 1971) + (year - 1969) // 4
#     days += sum(monthDays[:month-1])
#     days += 1 if month > 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) else 0
#     days += day
#     return res[(days + 3) % 7]
  
import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.datetime(year, month, day).strftime('%A')