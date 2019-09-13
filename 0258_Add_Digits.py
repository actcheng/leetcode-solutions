# Problem 258 
# Date completed: 2019/09/12

# 44 ms
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum([int(x) for x in str(num)])
        return num

# 32 ms
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        if num% 9 == 0: return 9
        return num % 9
        
