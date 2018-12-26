# Problem 693
# Date completed: 2018/12/26

# 64 ms
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #if n in [1,2]: return True
        a,b = divmod(n,2)
        while a > 0:
            a,c = divmod(a,2)
            if c == b: 
                return False
            else:
                b = c
            
        return  True
        
   
  # 56 ms
  class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #if n in [1,2]: return True
        #a,b = divmod(n,2)
        b = n % 2
        a = n // 2
        while a > 0:
            #a,c = divmod(a,2)
            c = a % 2
            if b == c: return False
            b = c
            a = a //2
                
        return  True
