# Problem 1237
# Date completed: 2019/12/03 

# 32 ms (95%)
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        y = 1
        l, r = 1,1000
        while l+1 < r:
            mid = (l+r)//2
            if customfunction.f(mid,y) <= z:
                l = mid
            else:
                r = mid
        
        x = l
        
        while x > 0 and y <= 1000:
            g = customfunction.f(x,y)
            if g == z: res.append([x,y])
            if g > z:
                x -= 1
            else:
                y += 1
                
        return res
        
        
