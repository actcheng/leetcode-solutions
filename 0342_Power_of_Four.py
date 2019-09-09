  
# Problem 342 
# Date completed: 2019/09/09

# 44 ms
def isPowerOfFour(self, num: int) -> bool:
        from math import log   
        if num > 0:
            return num == 4**(int(log(num)/log(4)))
        return False
