# Problem 1154
# Date completed: 2020/08/24 

# 32 ms (63%)
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = [int(d) for d in date.split('-')]
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0): 
            days[1] = 29
        return sum(days[:month-1]) + day

