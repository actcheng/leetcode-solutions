# Problem 172 
# Date completed: 2019/09/17

# 36 ms
class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 1
        zeros = 0
        while n >= 5**i :
            zeros += n // 5**i
            i += 1
        return zeros
