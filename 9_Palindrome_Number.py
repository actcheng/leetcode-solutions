# Solution 1 (312 ms)
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        if x<0:
            return False
        
        r=0
        y=x
        while y>0:
            r=r*10+y%10
            y=(y-y%10)/10
            
        return int(r)==x
