# Problem 70
# Date completed: 2019/10/07

# Dynamic programming solution
# 36 ms (67%)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2 : return 1

        steps = [0]*n

        steps[0] = 1
        steps[1] = 2
        for i in range(2,n):
            steps[i] = steps[i-1] + steps[i-2]
        
        return steps[n-1]

# Date completed: 2019/11/06
# 20 ms (100%)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2 : return 1
        prev2, prev = 1,2
        for i in range(2,n):
            prev2, prev = prev, prev+prev2        
        return prev
