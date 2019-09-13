# Problem 970
# Date completed: 2019/09/13

# 36 ms
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2: return 
        if x == 1 and y == 1: return [2]
        
        x, y = min(x,y), max(x,y)
        arr = []
        
        def increment(xi,j):
            num = xi + y**j
            if num <= bound:
                if num not in arr: arr.append(num)
                increment(xi,j+1)
        
        if x == 1:
            increment(1,0)
        else:
            
            i = 0
            while x**i + 1 <= bound:
                increment(x**i,0)
                i+= 1
     
        return arr    
            
