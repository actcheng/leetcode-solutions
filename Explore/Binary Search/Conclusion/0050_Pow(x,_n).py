# Problem 50
# Date completed: 2019/10/05 

# 172 ms (slow!)
# Using binary search -> not necessary!!
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        
        if n<0: x, n = 1/x, -n
            
        # Find greatest 2**n that is smaller/equal to n
        l,r = 0,n
        mid = 0
        while l+1<r:
            mid = (l+r)//2
            prod = 1<<mid
            if prod == n:
                l = mid
                break
            elif prod < n:
                l = mid
            else:
                r = mid
        k = 1<< l
        m = n-k
        
        res = x
        while k > 1:
            res = res*res
            k = k>>1
        return res*self.myPow(x,m)
        
# 24 ms sample solution
sample 24 ms submission
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1/x
        
        res = 1
        temp = x
        while n != 0:
            if n % 2 == 1:
                res = res * temp
            temp = temp * temp
            n = n // 2
        return res
    
# For example: x^13 = x^8 * x^4 * x^1

#  n      n % 2     temp     res
#  13       1        x        x
#  6        0        x^2      x
#  3        1        x^4      x * x^4
#  1        1        x^8      x * x^4 * x^8
