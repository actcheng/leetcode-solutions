# Problem 1137
# Date completed: 2020/01/09 

# 24 ms (82%)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1 or n==2:
            return 1
        
        prev = [0,1,1]
        for i in range(n-2):
            prev[0:2], prev[2] = prev[1:], sum(prev)
            
        return prev[2]
        
