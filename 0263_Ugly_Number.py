# Problem 263
# Date completed: 2019/09/12

# 40 ms
class Solution:
    def isUgly(self, num: int) -> bool:
        if num<=0: return False
        if num==1: return True
        factors = [2,3,5]
        for f in factors:
            while num%f==0:
                num /= f
                if num==1: return True
                
        return False
