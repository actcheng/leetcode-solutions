# Problem 231
# Date completed: 2019/12/18 

# 32 ms (67%)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        two = 1
        while n > two:
            two = two << 1
        
        return n == two

# 2020/06/08    
# 28 ms (85%)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return '1' not in bin(n).split('b')[-1][1:] if n > 0 else False
