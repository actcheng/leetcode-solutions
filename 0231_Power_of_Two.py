# Problem 231
# Date completed: 2019/12/18 

# 32 ms (67%)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        two = 1
        while n > two:
            two = two << 1
        
        return n == two
