# Problem 8
# Date completed: 2019/09/25

# 36 ms
class Solution:
    def myAtoi(self, str: str) -> int:
        start = False
        numString = ''
        pos = True
        for s in str:            
            if not start:
                if s == ' ': continue
                start = True
                if s == '-':
                    pos = False
                elif s == '+':
                    pos = True
                elif s.isdigit():
                    numString+=s
                else:
                    return 0            
            else:
                if s.isdigit():
                    numString+=s
                else:
                    break
        if numString == '': 
            return 0
        else:
            return min(2**31-1,int(numString)) if pos else -min(2**31,int(numString)) 
