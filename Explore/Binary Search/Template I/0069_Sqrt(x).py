# Problem 69
# Date completed: 2019/10/02 

# 40 ms (80%)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2: return x
        l, r = 1, x-1
        while l <= r:
            mid = l+(r-l)//2
            sq = mid**2
            if sq == x:
                return mid
            elif sq > x:                
                r = mid-1
            else:
                l = mid+1    
        return r
