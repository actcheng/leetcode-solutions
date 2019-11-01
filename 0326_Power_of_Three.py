# Problem 326
# Date completed: 2019/11/01 

# 128 ms (9%)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        from math import log
        return 3**int(round(log(n)/log(3))) == n
