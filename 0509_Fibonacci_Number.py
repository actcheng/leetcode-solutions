# Problem 509 
# Date completed: 2019/09/17

# 36 ms
class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1: return N
        prev2 = 0
        prev1 = 1
        for i in range(N-1):
            now = prev2+prev1
            prev2, prev1 = prev1, now
        
        return now
        
