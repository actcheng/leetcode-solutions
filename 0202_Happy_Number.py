# Problem 202
# Date completed: 2019/09/12

# 44 ms
class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        while n not in arr: 
            arr.append(n)
            n=sum([int(i)**2 for i in str(n)])              
        return n==1 
      
